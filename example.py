from datasets import WhiteBackgroundDataset

from transformers import AutoProcessor


dataset = WhiteBackgroundDataset(
    root="data",
    split="train",
    download=False,
    grid_size=3,
    processor=AutoProcessor.from_pretrained("/scratch1/wmz5132/models/huggingface/Llama-3.2-90B-Vision-Instruct"),
    process_fn="llama32",
    cutoff=100,
)

for x, y in dataset:
    print(x)
    print(y)
    break
