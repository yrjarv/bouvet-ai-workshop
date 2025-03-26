import os
import openai
from openai import AzureOpenAI

class LangueModelClient:
    def __init__(self):
        self.client = AzureOpenAI (
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01",
            azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment="gpt-4o-mini"
        )

    def generate_text(self, prompt: str) -> str:
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-4o-mini",
            )
            return chat_completion.choices[0].message.content
        
        except openai.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except openai.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except openai.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.message)