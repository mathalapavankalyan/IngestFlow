import uuid
from app.processors.file_processor import parse_file
from app.storage.dynamodb import store_document



def ingest_file(file_bytes: bytes , file_name: str)-> dict:
    parsed = parse_file(file_bytes , file_name)

    document_id = str(uuid.uuid4())
 
    metadata = {
        'file_name' : parsed['file_name'] , 
        'file_type' : parsed['file_type'] , 
        'field_count' : parsed['field_count'] , 
        'record_count' : parsed['record_count']
    }

    store_document(
        document_id=document_id,
        metadata=metadata,
        records=parsed["records"],
    )

    return {
        "document_id": document_id,
        "file_name": file_name,
        "record_count": parsed["record_count"],
    }