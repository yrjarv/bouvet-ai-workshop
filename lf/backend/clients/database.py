import os
from dataclasses import asdict
from typing import List

from azure.data.tables import TableServiceClient, TableEntity
from azure.core.credentials import AzureNamedKeyCredential
from model.recipe import Recipe


class Database:
    def __init__(self):
        api_key = os.getenv("AZURE_TABLE_API_KEY")
        credential = AzureNamedKeyCredential("abakusworkshop", api_key)
        service = TableServiceClient(endpoint="https://abakusworkshop.table.core.windows.net", credential=credential)
        self.client = service.get_table_client(table_name="recipes")

    def save_recipe(self, user_id: str, recipe: Recipe) -> Recipe:
        entity = asdict(recipe)

        entity["PartitionKey"] = user_id
        entity["RowKey"] = recipe.id

        entity["user_id"] = user_id
        entity["ingredients"] = ",".join(entity["ingredients"])

        self.client.create_entity(entity)

        return recipe

    def get_recipes(self, user_id) -> List[Recipe]:
        user_id_filter = f"PartitionKey eq '{user_id}'"

        try:
            result = self.client.query_entities(user_id_filter)

            recipe_list = []
            for item in result:
                # Map the Cosmos DB item to a RecipeData object
                recipe_data = Recipe(
                    id=item.get('id'),
                    recipeText=item.get('recipeText'),
                    imageUrl=item.get('imageUrl'),
                    ingredients=item.get('ingredients').split(",") or []
                )
                recipe_list.append(recipe_data)
            return recipe_list

        except Exception as e:
            return None
