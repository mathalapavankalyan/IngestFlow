from fastapi import APIRouter , UploadFile , File , HTTPException

from app.services.ingestion_service import ingest_file
from app.services.query_service import fetch_document
from app.models.response import IngestResponse , QueryResponse

router = APIRouter()

@router.post("/ingest" , response_model = IngestResponse)
async def ingest(file: UploadFile = File(...)):
    content = await file.read()

    return ingest_file(content , file.filename)

@router.get("/document/{document_id}", response_model=QueryResponse)
def get_document(document_id: str):
    result = fetch_document(document_id)

    if not result["found"]:
        raise HTTPException(status_code=404, detail="Document not found")

    return result