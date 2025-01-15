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
        entity = dict()

        entity["imageUrl"] = recipe.imageUrl
        entity["recipeText"] = recipe.recipeText
        entity["id"] = recipe.id
        entity["ingredients"] = ",".join(recipe.ingredients)

        # PartitionKey and RowKey are required by Azure Table Service to organize and index data.
        # PartitionKey groups related entities (in this case, all recipes for a specific user),
        # and RowKey uniquely identifies each entity within that partition.
        entity["PartitionKey"] = user_id
        entity["RowKey"] = recipe.id

        self.client.create_entity(entity)

        return recipe

    def get_recipes(self, user_id) -> List[Recipe]:
        user_id_filter = f"PartitionKey eq '{user_id}'"

        try:
            result = self.client.query_entities(user_id_filter)
            # TODO - oppgave 3.2 return a list of recipes
            # https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python#querying-entities
            return []

        except Exception as e:
            return None
