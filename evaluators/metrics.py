from typing import List

from .utils import clean_response, complexgrid_parse


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


def default_complexgrid_metrics(responses: List[dict], labels: List[dict]) -> dict:
    eval_results = []

    for response, label in zip(responses, labels):
        id, row, col = label["id_row_col"].split("_")
        row_ans, col_ans = int(row) + 1, int(col) + 1
        row_resp, col_resp = complexgrid_parse(response["response"])
        score = 1 if row_resp == row_ans and col_resp == col_ans else 0

        eval_results.append({
            "id_row_col": label["id_row_col"],
            "question": response["metadata"]["question"],
            "answer": f'row: {row_ans}, col: {col_ans}',
            "response": response["response"],
            "parsed_response": f'row: {row_resp}, col: {col_resp}',
            "score": score
        })

    return eval_results
