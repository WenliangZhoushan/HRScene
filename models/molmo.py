from .base import BaseModel

import torch
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig


class Molmo(BaseModel):
    def __init__(self, model_path: str, **model_kwargs) -> None:
        super().__init__(model_path, **model_kwargs)
        self.device = self.model.device


    def _init_model(self, model_path: str, **model_kwargs) -> None:
        self.model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)
        self.processor = AutoProcessor.from_pretrained(model_path)


    def process_inputs(self, inputs: dict) -> dict:
        image_path = inputs["image_path"]
        image = Image.open(image_path)
        
        inputs = self.processor.process(images=[image], text=inputs["question"])
        inputs["images"] = inputs["images"].to(torch.bfloat16)
        inputs = {k: v.to(self.device).unsqueeze(0) for k, v in inputs.items()}

        return inputs
    

    def generate(self, inputs: dict, **generation_kwargs) -> str:
        with torch.autocast(device_type="cuda", enabled=True, dtype=torch.bfloat16):
            output = self.model.generate_from_batch(
                inputs, GenerationConfig(**generation_kwargs), tokenizer=self.processor.tokenizer
            )
            generated_tokens = output[0, inputs['input_ids'].size(1):]
            response = self.processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)
            print(response)
        return response
