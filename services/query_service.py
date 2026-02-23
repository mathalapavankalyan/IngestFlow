from app.storage.dynamodb import get_document


def fetch_document(document_id : str)-> dict:
    result = get_document(document_id)

    if result is None:
        return {'found' : False}
    return {
        'found'  :True,
        **result
    }