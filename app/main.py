import boto3
from fastapi import FastAPI, HTTPException
from typing import List
from models import Recipe
import crud
import uvicorn


# print(boto3.__version__)
# all the endpoints are being defined here

app = FastAPI()
@app.get("/")
def read_root():
    return {'message': 'Welcome to my Meal Planner API'}

@app.get("/recipes/{meal_type}", response_model=List[Recipe])
def get_recipe(meal_type: str):
    recipes = crud.get_recipe(meal_type)
    if not recipes:
        raise HTTPException(status_code=404, detail="Meal type not found")
    return recipes

@app.post("/recipes/{meal_type}", response_model=Recipe)
def post_recipe(meal_type:str , recipe:Recipe):
   created_recipe = crud.add_recipe(meal_type, recipe)
   if not created_recipe:
        raise HTTPException(status_code=500, detail="Error creating recipe")
   return created_recipe
  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

