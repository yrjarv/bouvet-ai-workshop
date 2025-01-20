from dataclasses import dataclass

from werkzeug.datastructures import FileStorage

from clients.database import Database
from clients.image_generator_client import ImageGeneratorClient
from clients.image_recognition_client import ImageRecognitionClient
from clients.llm_client import LangueModelClient
from model.recipe import Recipe
import uuid


def recipe_prompt(ingredients: list[str]):
    return f"""
You are a master chef.
            Please create a recipe based on the following ingredients. The following ingredient(s) is all that i have in my fridge: {", ".join(ingredients)}.

Requirements:
- Provide a short, catchy recipe name.
- First line of the output is the recipe name
- Provide only the recipe, no extra chit chat
- Be snarky about the state of the users fridge
- Include a brief introduction or backstory (one or two sentences).
- List ingredients with approximate measurements, in metric.
- Provide step-by-step cooking instructions.
- Suggest additional tips, serving suggestions, or variations.
- Include estimated prep and cook times.
- Assume the user doesnt have much more than the provided ingredients, apart from some very basic pantry items
- The output should be formatted in markdown

Keep it clear, concise, and fun to read.
"""


def image_prompt(recipe: str):
    return f"""
        Create a beautiful image of the dish described in this recipe.
        This is only a photo of food!

        RECIPE:
        {recipe}
    """


@dataclass
class RecipeGenerator:
    image_recognition_client: ImageRecognitionClient
    llm_client: LangueModelClient
    image_generation_client: ImageGeneratorClient

    def generate_recipe(self, tags: list[str]):
        recipe = self.llm_client.generate_text(recipe_prompt(tags))
        imageUrl = self.image_generation_client.generate_image(
            image_prompt(recipe))
        unique_id = str(uuid.uuid4())

        recipeData = Recipe(
            unique_id,
            recipe,
            imageUrl,
            tags
        )

        return recipeData
