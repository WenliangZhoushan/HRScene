from typing import List

from .utils import clean_response, realworld_parse


def default_realworld_metrics(responses: List[dict], labels: List[dict]) -> dict:
    eval_results = []

    for response, label in zip(responses, labels):
        prediction, matched = realworld_parse(response["response"])
        if matched and prediction == label:
            score = 1
        else:
            prediction = clean_response(response["response"])
            prediction = prediction.replace("</ans>", "").replace("<ans>", "").strip()
            score = 1 if prediction.lower() == label.lower() else 0

        eval_results.append({
            "id": response["metadata"]["id"],
            "question": response["metadata"]["question"],
            "answer": label,
            "response": response["response"],
            "score": score
        })

    return eval_results
