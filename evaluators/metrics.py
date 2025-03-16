from typing import List

from .utils import clean_response


def default_whitebackground_metrics(responses: List[dict], labels: List[dict]) -> dict:
    eval_results = []

    for response, label in zip(responses, labels):
        prediction = clean_response(response["response"])
        score = min(sum(ans.lower() in prediction.lower() for ans in label["answer"]) / 3, 1) if prediction else 0

        eval_results.append({
            "id_row_col": label["id_row_col"],
            "question": response["metadata"]["question"],
            "answer": label["answer"],
            "response": response["response"],
            "score": score
        })

    return eval_results
