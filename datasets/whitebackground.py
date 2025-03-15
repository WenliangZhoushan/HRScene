import json
import os
from typing import Any, List, Literal, Tuple

from .base import BaseDataset
from prompts import whitebackground_prompt

WHITEBACKGROUND_PROMPT = whitebackground_prompt()


class WhiteBackgroundDataset(BaseDataset):
    def __init__(
            self, root: str, split: Literal["test"], download: bool, grid_size: int, num_samples: int = 500
        ) -> None:
        self.grid_size = grid_size
        self.num_samples = num_samples
        super().__init__(root, split, download)


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
        json_inputs = json.load(open(json_path))[:self.num_samples]
        image_dir = os.path.join(self.root, "whitebackground", self.split, f"{self.grid_size}x{self.grid_size}")

        for idx, line in enumerate(json_inputs):
            for i in range(self.grid_size * self.grid_size):
                row_idx, col_idx = i // self.grid_size, i % self.grid_size
                data.append({
                    "question": f'{line["question"]}\n Answer as concise as possible, just a few words.',
                    "image_path": os.path.join(image_dir, str(idx), f"grid_{row_idx}_{col_idx}.jpg"),
                })
                targets.append(line["answer"])

        return data, targets
    

    def __getitem__(self, idx: int) -> Tuple[dict[str, Any], List[str]]:
        return self.data[idx], self.targets[idx]
