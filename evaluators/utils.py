def clean_response(response: str) -> str:
    if not response:
        return ""
    response = response.split('\n')[-1].lower().replace('answer:', "").replace('*', "").replace('.', "").strip()
    
    return response
