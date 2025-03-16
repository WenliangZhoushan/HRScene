from datasets import ComplexGridDataset, WhiteBackgroundDataset
from models import GPT, Llama32
from tester import ComplexGridTester, WhiteBackgroundTester

import torch


dataset = WhiteBackgroundDataset(root="data", split="test", download=False, grid_size=5, num_samples=150)
model = Llama32(model_path='meta-llama/Llama-3.2-11B-Vision', torch_dtype=torch.bfloat16, device_map="cuda")
tester = WhiteBackgroundTester(model, dataset)
tester.run()
tester.eval()

dataset = ComplexGridDataset(root="data", split="test", download=False, grid_size=3, num_samples=200)
model = GPT(model_path="gpt-4o-mini")
tester = ComplexGridTester(model, dataset)
tester.run()
tester.eval()
