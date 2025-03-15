import importlib
import json
import os
from typing import Any, Callable, List, Tuple

from .base import BaseDataset
from prompts import whitebackground_prompt

from transformers import AutoProcessor

WHITEBACKGROUND_PROMPT = whitebackground_prompt()


class WhiteBackgroundDataset(BaseDataset):
    def __init__(
            self, root: str, split: str, download: bool, 
            grid_size: int, processor: AutoProcessor, process_fn: str | Callable, cutoff: int = 500
        ) -> None:
        self.grid_size = grid_size
        self.cutoff = cutoff
        self.processor = processor
        super().__init__(root, split, download)

        if isinstance(process_fn, str):
            self.process_fn = getattr(importlib.import_module("process_functions"), process_fn)
        else:
            self.process_fn = process_fn


    def _download_and_check_data(self) -> None:
        # TODO: after publishing the dataset to huggingface, add the download logic here
        pass


    def _check_exists(self) -> bool:
        exists = os.path.exists(
            os.path.join(self.root, "whitebackground", self.split, f"{self.grid_size}x{self.grid_size}")
        )

        return exists


    def _load_data(self) -> Tuple[List[dict[str, Any]], List[List[str]]]:
        data, targets = [], []

        json_path = os.path.join(self.root, "whitebackground", self.split, "data.json")
        json_inputs = json.load(open(json_path))[:self.cutoff]
        image_dir = os.path.join(self.root, "whitebackground", self.split, f"{self.grid_size}x{self.grid_size}")

        for idx, line in enumerate(json_inputs):
            for i in range(self.grid_size * self.grid_size):
                row_idx, col_idx = i // self.grid_size, i % self.grid_size
                data.append({
                    "question": line["question"],
                    "image_path": os.path.join(image_dir, str(idx), f"grid_{row_idx}_{col_idx}.jpg"),
                })
                targets.append(line["answer"])

        return data, targets
    

    def __getitem__(self, idx: int) -> Tuple[dict[str, Any], List[str]]:
        data, target = self.data[idx], self.targets[idx]

        inputs = self.process_fn(data, self.processor, WHITEBACKGROUND_PROMPT)
        x = {"inputs": inputs, "question": data["question"], "image_path": data["image_path"]}
        y = target

        return x, y
