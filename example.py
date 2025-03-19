from models import GPT, Llama32
from tester import DiagnosisTester
import torch


# Example 1: Run 150 complexgrid_3x3 samples on local model
model = Llama32(model_path="meta-llama/Llama-3.2-11B-Vision-Instruct", torch_dtype=torch.bfloat16, device_map="cuda")
tester = DiagnosisTester(model=model, dataset_name="complexgrid_3x3", num_samples=150)
tester.run()
tester.eval()


# Example 2: Run complete whitebackground_7x7 samples on remote model
model = GPT(model_path="gpt-4o-mini")
tester = DiagnosisTester(model=model, dataset_name="whitebackground_7x7")
tester.run()
tester.eval()
