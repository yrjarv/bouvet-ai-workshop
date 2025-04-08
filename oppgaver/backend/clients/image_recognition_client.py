from typing import List
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv
from io import BytesIO

class ImageRecognitionClient:
    def __init__(self):
        # Set up credentials and endpoint
        self.prediction_key = os.getenv("AZURE_CUSTOM_VISION_PRED_KEY")
        self.endpoint = os.getenv("AZURE_CUSTOM_VISION_ENDPOINT")
        self.project_id = os.getenv("AZURE_CUSTOM_VISION_PROJECT_ID")
        self.iteration_name = os.getenv("AZURE_CUSTOM_VISION_ITERATION")

        if not all([self.prediction_key, self.endpoint, self.project_id, self.iteration_name]):
            raise ValueError("Missing one or more required environment variables!")

    def recognize_ingredients(self, image: BytesIO) -> List[str]:
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.prediction_key})
        predictor = CustomVisionPredictionClient(self.endpoint, credentials)
        try:
            # Make the prediction
            results = predictor.detect_image(
                    self.project_id,
                    self.iteration_name,
                    image.read()
                )

            predictions = [(prediction.tag_name.lower()) 
                           for prediction in results.predictions
                           if prediction.probability >= 0.6
                        ]
            unique_ingredients = list(dict.fromkeys(predictions))
            return unique_ingredients

        except FileNotFoundError:
            print(f"Error: File not found at path '{image}'")
        except Exception as e:
            print(f"Error: {e}")
