from dataclasses import dataclass
from typing import List


@dataclass
class Recipe:
    id: str
    recipeText: str
    imageUrl: str
    ingredients: List[str]
