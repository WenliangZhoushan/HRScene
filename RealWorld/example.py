import os
os.environ['HF_HOME'] = '/scratch1/wmz5132/HRScenne/data/huggingface'
os.environ['HF_DATASETS_CACHE'] = '/scratch1/wmz5132/HRScenne/data/huggingface'

from models import GPT,Llama32
from tester import RealWorldTester
import torch


model = GPT(model_path="gpt-4o-mini")
tester = RealWorldTester(model=model, dataset_name="ArtBench", split="validation", num_samples=5)
tester.run(max_tokens=100)
tester.eval()

# model = Llama32(model_path="/scratch1/wmz5132/models/huggingface/Llama-3.2-11B-Vision-Instruct", torch_dtype=torch.bfloat16, device_map="cuda")
# tester = RealWorldTester(model=model, dataset_name="ArtBench", split="test_mini", num_samples=5)
# tester.run(max_new_tokens=100)
# tester.eval()
