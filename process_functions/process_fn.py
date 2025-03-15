from typing import Any

import torch
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from transformers import AutoProcessor


def llama32(data: dict[str, Any], processor: AutoProcessor, prompt: str) -> dict[str, torch.Tensor]:
    image_path = data["image_path"]
    image = Image.open(image_path)

    prompt = prompt.format(question=data["question"])
    message = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": prompt}
            ],
        }
    ]
    message = processor.apply_chat_template(message, add_generation_prompt=True)

    inputs = processor(image, message, add_special_tokens=False, return_tensors="pt")

    return inputs
