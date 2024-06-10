from pydantic import BaseModel
from typing import List

# it uses the BaseModel class from the Pydalint library to ensure that every instance of the Recipe class 
# Using the concept of inheritance, the Recipe Class inherits from the BaseModel thereby getting all its features including data validation
class Recipe(BaseModel):
    # declaring the attributes that will be used and it's type
    id : str
    name: str
    picture: str
    ingredients: List[str]
    instructions: List[str]

class RecipeCreate(BaseModel):
    name: str
    picture: str
    ingredients: List[str]
    instructions: List[str]