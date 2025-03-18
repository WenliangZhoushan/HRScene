import os
from typing import Any, Tuple

from torch.utils.data import Dataset


class BaseDataset(Dataset):
    def __init__(self, root: str, split: str, download: bool = False):
        super().__init__()
        self.root = root
        self.split = split

        if download:
            self._download_and_check_data()
        if not self._check_exists():
            raise FileNotFoundError(f"Dataset not found. You can use download=True to download it.")
        
        self.data, self.targets = self._load_data()
    
    
    def _download_and_check_data(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")


    def _check_exists(self) -> bool:
        exists = os.path.exists(os.path.join(self.root, self.split))

        return exists


    def _load_data(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")
    

    def __len__(self) -> int:
        return len(self.data)


    def __getitem__(self, idx: int) -> Tuple[Any, Any]:
        return self.data[idx], self.targets[idx]
