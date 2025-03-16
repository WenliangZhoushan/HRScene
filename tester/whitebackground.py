import json
import os
import time
from typing import Callable

from .base import BaseTester
from datasets.base import BaseDataset
from evaluators import default_whitebackground_metrics
from models.base import BaseModel

import numpy as np
from tqdm import tqdm


class WhiteBackgroundTester(BaseTester):
    def __init__(self, model: BaseModel, dataset: BaseDataset) -> None:
        super().__init__(model, dataset)
        self.responses = []
        self.labels = []


    def run(self, **generation_kwargs) -> None:
        for x, y in tqdm(self.dataset, desc='Inferencing WhiteBackground'):
            inputs = self.model.process_inputs(x)
            response = self.model.generate(inputs, **generation_kwargs)
            # remove the question from the response if it exists
            response = response.split(x["question"])[-1]
            response = {
                "response": response,
                "metadata": x
            }

            self.responses.append(response)
            self.labels.append(y)


    def eval(self, eval_results_dir: str | None = None, metrics: str | Callable = "default") -> None:
        if not eval_results_dir:
            eval_results_dir = os.path.join("results", "whitebackground", time.strftime("%Y%m%d_%H%M%S"))
        os.makedirs(eval_results_dir, exist_ok=True)
        if metrics == "default":
            metrics = default_whitebackground_metrics
        else:
            metrics = metrics

        eval_results = metrics(self.responses, self.labels)
        scores = np.array([result["score"] for result in eval_results])
        
        with open(os.path.join(eval_results_dir, "eval_results.jsonl"), "w") as f:
            for result in eval_results:
                f.write(json.dumps(result) + "\n")
        
        with open(os.path.join(eval_results_dir, "eval_scores.txt"), "w") as f:
            f.write(f"Average score: {scores.mean()}\n")
            f.write(f"Median score: {np.median(scores)}\n")
            f.write(f"Standard deviation: {scores.std()}\n")
        
        return
