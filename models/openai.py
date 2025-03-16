import base64
from .base import BaseModel

from openai import OpenAI


class GPT(BaseModel):
    MODEL_NAME = "GPT"

    def __init__(self, model_path: str, **model_kwargs) -> None:
        super().__init__(model_path, **model_kwargs)
        self.model = model_path


    def _init_model(self, model_path: str, **model_kwargs) -> None:
        self.client = OpenAI(**model_kwargs)


    def process_inputs(self, inputs: dict) -> dict:
        image_path = inputs["image_path"]
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        if "image_type" in inputs:
            image_type = inputs["image_type"]
        else:
            image_type = image_path.split(".")[-1].lower()
            image_type = "jpeg" if image_type == "jpg" else image_type

        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": inputs["question"]}, 
                {"type": "image_url", "image_url": {"url": f"data:image/{image_type};base64,{base64_image}"}}
            ]
        }]

        return messages
    

    def generate(self, inputs: dict, **generation_kwargs) -> str:
        output = self.client.chat.completions.create(model=self.model, messages=inputs, **generation_kwargs)
        response = output.choices[0].message.content

        return response
