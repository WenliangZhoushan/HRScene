from typing import Callable

from datasets.base import BaseDataset
from models.base import BaseModel


class BaseTester:
    def __init__(self, model: BaseModel, dataset: BaseDataset) -> None:
        self.model = model
        self.dataset = dataset


    def run(self, **generation_kwargs) -> None:
        raise NotImplementedError
    

    def eval(self, eval_results_dir: str, metrics: str | Callable) -> None:
        raise NotImplementedError
