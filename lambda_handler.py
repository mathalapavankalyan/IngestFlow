import boto3
from mangum import Mangum
from fastapi import FastAPI
from app.api.routes import router
from app.services.ingestion_service import ingest_file

s3 = boto3.client("s3")

app = FastAPI(title="Ingestion Platform")
app.include_router(router)

http_handler = Mangum(app)

def lambda_handler(event, context):
    # 🔹 Handle S3-triggered ingestion
    if isinstance(event, dict) and "Records" in event:
        # Extra safety: ensure it's really an S3 event
        if event["Records"] and "s3" in event["Records"][0]:
            for record in event["Records"]:
                bucket = record["s3"]["bucket"]["name"]
                key = record["s3"]["object"]["key"]

                obj = s3.get_object(Bucket=bucket, Key=key)
                file_bytes = obj["Body"].read()

                ingest_file(file_bytes, key)

            return {"status": "S3 ingestion completed"}

    # Ignore Lambda console test events / unknown events
    if not isinstance(event, dict) or "requestContext" not in event:
        return {"status": "Non-HTTP event ignored"}

    # Handle HTTP API requests (API Gateway)
    return http_handler(event, context)
