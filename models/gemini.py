from .base import BaseModel

from google import genai
from google.genai import types


class Gemini(BaseModel):
    def __init__(self, model_path: str, **model_kwargs) -> None:
        super().__init__(model_path, **model_kwargs)
        self.model = model_path


    def _init_model(self, model_path: str, **model_kwargs) -> None:
        self.client = genai.Client(**model_kwargs)


    def process_inputs(self, inputs: dict) -> dict:
        image_path = inputs["image_path"]
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
        if "image_type" in inputs:
            image_type = inputs["image_type"]
        else:
            image_type = image_path.split(".")[-1].lower()
            image_type = "jpeg" if image_type == "jpg" else image_type
        
        content = [
            inputs["question"],
            types.Part.from_bytes(data=image_bytes, mime_type=f'image/{image_type}')
        ]

        return content


    def generate(self, inputs: dict, **generation_kwargs) -> str:
        output = self.client.models.generate_content(model=self.model, contents=inputs, **generation_kwargs)
        response = output.text

        return response
