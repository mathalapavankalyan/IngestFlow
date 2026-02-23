import json

def parse_file(file_bytes: bytes, file_name: str) -> dict:
    file_type = file_name.rsplit(".", 1)[-1].lower()

    if file_type == "json":
        try:
            decoded = file_bytes.decode(errors="ignore")
            data = json.loads(decoded)
        except Exception:
            data = {"raw": decoded}
    else:
        data = {"raw": file_bytes.decode(errors="ignore")}

    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        records = [{"raw": str(data)}]

    field_count = (
        len(records[0]) if records and isinstance(records[0], dict) else 0
    )

    return {
        "file_name": file_name,
        "file_type": file_type,
        "record_count": len(records),
        "field_count": field_count,
        "records": records,
    }
