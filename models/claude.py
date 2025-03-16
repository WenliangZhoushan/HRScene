import base64
from .base import BaseModel

from anthropic import Anthropic


class Claude(BaseModel):
    MODEL_NAME = "Claude"

    def __init__(self, model_path: str, **model_kwargs) -> None:
        super().__init__(model_path, **model_kwargs)
        self.model = model_path

    
    def _init_model(self, model_path: str, **model_kwargs) -> None:
        self.client = Anthropic(**model_kwargs)


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
                {"type": "image", "source": {"type": "base64", "media_type": f'image/{image_type}', "data": base64_image}},
                {"type": "text", "text": inputs["question"]}
            ],
        }]

        return messages
    

    def generate(self, inputs: dict, **generation_kwargs) -> str:
        max_tokens = generation_kwargs.get("max_tokens", 200)

        output = self.client.messages.create(
            model=self.model, max_tokens=max_tokens, messages=inputs, **generation_kwargs
        )
        response = output.content[0].text

        return response
