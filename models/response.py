from pydantic import BaseModel

from typing import Any , List , Optional

class IngestResponse(BaseModel) : 
    document_id : str
    file_name : str
    record_count : int

class QueryResponse(BaseModel):
    found:bool
    metadata: Optional[dict] = None
    record_count: Optional[int] = None
    records: Optional[Any]   = None
    