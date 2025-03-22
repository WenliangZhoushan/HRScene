import re
from typing import Tuple


def clean_response(response: str) -> str:
    if not response:
        return ""
    response = response.split('\n')[-1].lower().replace('answer:', "").replace('*', "").replace('.', "").strip()
    
    return response


def realworld_parse(response: str) -> Tuple[int, int]:
    pattern = re.compile(r"<ans>(.*?)<\/ans>")
    matches = pattern.findall(response)
    if matches:
        answer = matches[0], True
    else:
        answer = "", False
        
    return answer
