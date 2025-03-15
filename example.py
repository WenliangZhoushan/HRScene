from datasets import WhiteBackgroundDataset
from models import Llama32
from tester import WhiteBackgroundTester

import torch


dataset = WhiteBackgroundDataset(root="data", split="test", download=False, grid_size=3, num_samples=5)
model = Llama32(
    model_path="/scratch1/wmz5132/models/huggingface/Llama-3.2-11B-Vision",
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
)
tester = WhiteBackgroundTester(model, dataset)
tester.run()
tester.eval(eval_results_dir="results/whitebackground", metrics="default")
