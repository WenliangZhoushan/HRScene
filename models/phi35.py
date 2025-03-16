from .base import BaseModel

import torch
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from transformers import AutoModelForCausalLM, AutoProcessor


class Phi35(BaseModel):
    def __init__(self, model_path: str, **model_kwargs) -> None:
        super().__init__(model_path, **model_kwargs)
        self.device = self.model.device


    def _init_model(self, model_path: str, **model_kwargs) -> None:
        model_kwargs["trust_remote_code"] = model_kwargs.get("trust_remote_code", True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)
        self.processor = AutoProcessor.from_pretrained(model_path, **model_kwargs)


    def process_inputs(self, inputs: dict) -> dict:
        image_path = inputs["image_path"]
        image = Image.open(image_path)

        messages = [
            {"role": "user", "content": "<|image_1|>\n" + inputs["question"]},
        ]
        message: dict = self.processor.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

        inputs = self.processor(message, [image], return_tensors="pt")
        inputs = inputs.to(self.device)

        return inputs
    
    
    def generate(self, inputs: dict, **generation_kwargs) -> str:
        with torch.inference_mode():
            generate_ids = self.model.generate(
                **inputs, eos_token_id=self.processor.tokenizer.eos_token_id, **generation_kwargs
            )
            generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]
            response = self.processor.batch_decode(
               generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )[0]

        return response
