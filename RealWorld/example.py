import os
os.environ['HF_HOME'] = '/scratch1/wmz5132/HRScenne/data/huggingface'
os.environ['HF_DATASETS_CACHE'] = '/scratch1/wmz5132/HRScenne/data/huggingface'

from models import GPT,Llama32
from tester import RealWorldTester
import torch

# example 1: use api based model to run 5 samples of ArtBench subset
model = GPT(model_path="gpt-4o-mini")
tester = RealWorldTester(model=model, dataset_name="ArtBench", split="validation", num_samples=5)
tester.run(max_tokens=100)
tester.eval()

# example 2: use local llama32 model to run complete realworld dataset
model = Llama32(model_path="meta-llama/Llama-3.2-11B-Vision-Instruct", torch_dtype=torch.bfloat16, device_map="cuda")
tester = RealWorldTester(model=model, dataset_name="ArtBench", split="test")
tester.run(max_new_tokens=100)
tester.eval()
