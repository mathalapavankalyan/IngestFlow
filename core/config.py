import os

def get_env(name: str , default: str | None = None) -> str:
    value = os.getenv(name , default)
    if value is None:
        raise RuntimeError(f'Missing required environment variable: {name}')
    return value

# DynamoDB

DYNAMODB_TABLE  = get_env("DYNAMODB_TABLE")
DYNAMODB_PK = get_env("DYNAMODB_PK", "pk")
DYNAMODB_SK = get_env("DYNAMODB_SK", "sk")

# Key prefixes

DOC_PK_PREFIX = get_env("DOC_PK_PREFIX" , "DOCUMENT#")
CHUNK_SK_PREFIX = get_env("CHUNK_SK_PREFIX", "PART#")


# Limits
MAX_CHUNK_SIZE = int(get_env("MAX_CHUNK_SIZE" , "300000"))


