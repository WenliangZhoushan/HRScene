import json
import os
import time
from typing import Callable

from .base import BaseTester
from hrscene_datasets.base import BaseDataset
from evaluators import default_complexgrid_metrics, draw_heatmap
from models.base import BaseModel

import numpy as np
from tqdm import tqdm


class ComplexGridTester(BaseTester):
    def __init__(self, model: BaseModel, dataset: BaseDataset) -> None:
        super().__init__(model, dataset)
        self.responses = []
        self.labels = []
        self.model_name = getattr(self.model, "MODEL_NAME", "Custom Model")
        self.experiment_name = f"ComplexGrid {self.model_name} {self.dataset.grid_size}x{self.dataset.grid_size}"


    def run(self, **generation_kwargs) -> None:
        for x, y in tqdm(self.dataset, desc='Inferencing ComplexGrid'):
            inputs = self.model.process_inputs(x)
            response = self.model.generate(inputs, **generation_kwargs)
            response = {
                "response": response,
                "metadata": x
            }

            self.responses.append(response)
            self.labels.append(y)


    def eval(self, eval_results_dir: str | None = None, metrics: str | Callable = "default") -> None:
        if not eval_results_dir:
            eval_results_dir = os.path.join("results", "complexgrid", time.strftime("%Y%m%d_%H%M%S"))
        os.makedirs(eval_results_dir, exist_ok=True)
        if metrics == "default":
            metrics = default_complexgrid_metrics
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
        
        draw_heatmap(eval_results, self.dataset.grid_size, self.experiment_name, eval_results_dir)

        print(f"Finished evaluation for experiment: {self.experiment_name}")
        print(f'- Model: {self.model_name}')
        print(f'- Dataset: ComplexGrid {self.dataset.grid_size}x{self.dataset.grid_size}')
        print(f'- Average score: {float(scores.mean()):.2f}')
        print(f'- Median score: {float(np.median(scores)):.2f}')
        print(f'- Standard deviation: {float(scores.std()):.2f}')
        print(f'- Results saved in: {eval_results_dir}')
