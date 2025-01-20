from dataclasses import dataclass

from clients.image_generator_client import ImageGeneratorClient
from clients.image_recognition_client import ImageRecognitionClient
from clients.llm_client import LangueModelClient
from model.recipe import Recipe
import uuid


def recipe_prompt(ingredients: list[str]):
    return f"""
You are a bad chef.
Please create some sort of recipe based on the following ingredients.
Don't bother being clever or precise—just wing it.
The following ingredient(s) is all that i have in my fridge: {", ".join(ingredients)}.

Requirements:
- First line of the output is the recipe name
- The output should be formatted in markdown
"""


def image_prompt(recipe: str):
    return f"""
        Just slap together some low-effort, boring photo of the dish described in this recipe.
        Seriously, don't try too hard. No fancy plating or lighting—make it dull.

        RECIPE:
        {recipe}
    """


@dataclass
class RecipeGenerator:
    image_recognition_client: ImageRecognitionClient
    llm_client: LangueModelClient
    image_generation_client: ImageGeneratorClient

    def generate_recipe(self):
        # TODO oppgave 2.2 - call azure and return real data

        unique_id = str(uuid.uuid4())

        recipe = Recipe(
            unique_id,
            f"""
                Havregrøt

                Ingredienser:

                1 dl havregryn
                2 dl melk/vann

                Fremgangsmåte:
                Kok opp, rør i 3-5 min.
            """,
            "https://placehold.co/600x400",
            ["havregryn, melk"]
        )

        return recipe
