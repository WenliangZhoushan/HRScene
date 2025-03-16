import importlib
import os
from typing import Callable

from .base import BaseTester
from datasets.base import BaseDataset
from models.base import BaseModel

from tqdm import tqdm


class ComplexGridTester(BaseTester):
    def __init__(self, model: BaseModel, dataset: BaseDataset) -> None:
        super().__init__(model, dataset)
        self.responses = []
        self.labels = []


    def run(self, **generation_kwargs) -> None:
        for x, y in tqdm(self.dataset, desc='Inferencing ComplexGrid'):
            inputs = self.model.process_inputs(x)
            response = self.model.generate(inputs, **generation_kwargs)

            self.responses.append(response)
            self.labels.append(y)


    def eval(self, eval_results_dir: str, metrics: str | Callable) -> None:
        os.makedirs(eval_results_dir, exist_ok=True)
        if isinstance(metrics, str):
            metrics = getattr(importlib.import_module("evaluators"), metrics)
        else:
            metrics = metrics

        # TODO: a dummy evaluation, add real evaluation logic
        scores = 0
        for response, label in zip(self.responses, self.labels):
            scores += metrics(response, label)
        
        return scores / len(self.responses)
