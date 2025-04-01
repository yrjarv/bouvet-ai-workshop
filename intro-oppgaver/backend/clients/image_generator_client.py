import openai
from openai import AzureOpenAI
import os

class ImageGeneratorClient:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-07-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment="dall-e-3"
        )

    def generate_image(self, prompt: str) -> str:
        try:
            response = self.client.images.generate(
                model="PUT_YOUR_MODEL_HERE",  # TODO: oppgave 2.1.2 Sett riktig modell her
                prompt=prompt,
                size="0",  # TODO: oppgave 2.1.3 Sett riktig størrelse her
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            return image_url

        # catch exceptions
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.message)
