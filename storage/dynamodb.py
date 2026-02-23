# app/storage/dynamodb.py
import boto3
import json
from decimal import Decimal
from typing import Any
from boto3.dynamodb.conditions import Key
from app.core.config import (
    DYNAMODB_TABLE,
    DYNAMODB_PK,
    DYNAMODB_SK,
    DOC_PK_PREFIX,
    CHUNK_SK_PREFIX,
    MAX_CHUNK_SIZE,
)

# 🔹 Helper defined in SAME FILE (no import!)
def to_dynamodb_compatible(value: Any):
    if isinstance(value, float):
        return Decimal(str(value))
    elif isinstance(value, dict):
        return {k: to_dynamodb_compatible(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [to_dynamodb_compatible(v) for v in value]
    else:
        return value


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DYNAMODB_TABLE)


def estimate_size(obj) -> int:
    return len(json.dumps(obj, ensure_ascii=False).encode("utf-8"))


def chunk_records(records: list):
    chunk, size = [], 0
    for record in records:
        record_size = estimate_size(record)
        if size + record_size > MAX_CHUNK_SIZE:
            yield chunk
            chunk, size = [], 0
        chunk.append(record)
        size += record_size
    if chunk:
        yield chunk


def build_pk(document_id: str) -> str:
    return f"{DOC_PK_PREFIX}{document_id}"


def build_sk(chunk_index: int) -> str:
    return f"{CHUNK_SK_PREFIX}{chunk_index}"


def store_document(document_id: str, metadata: dict, records: list):
    pk = build_pk(document_id)

    with table.batch_writer() as batch:
        for idx, chunk in enumerate(chunk_records(records)):
            batch.put_item(
                Item={
                    DYNAMODB_PK: pk,
                    DYNAMODB_SK: build_sk(idx),
                    "chunk_index": idx,
                    "metadata": to_dynamodb_compatible(metadata),
                    "records": to_dynamodb_compatible(chunk),
                }
            )


def get_document(document_id: str) -> dict | None:
    response = table.query(
        KeyConditionExpression=Key(DYNAMODB_PK).eq(build_pk(document_id))
    )
    items = response.get("Items", [])
    if not items:
        return None

    items.sort(key=lambda x: x["chunk_index"])
    records, metadata = [], items[0]["metadata"]
    for item in items:
        records.extend(item["records"])

    return {
        "metadata": metadata,
        "records": records,
        "record_count": len(records),
    }
