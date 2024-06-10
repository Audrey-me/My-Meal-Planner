import boto3
from boto3.dynamodb.conditions import Key
from models import Recipe, RecipeCreate
from botocore.exceptions import ClientError
from models import Recipe
from uuid import uuid4


# crud operation to interact with dynamodb table created
dynamodb = boto3.resource('dynamodb', region_name ='us-east-1')
table = dynamodb.Table('Recipes')
        
def get_recipe(meal_type: str):
    try:
        response = table.scan(
            FilterExpression='meal_type = :meal_type',
            ExpressionAttributeValues={':meal_type': meal_type}
        )
        return [Recipe(**item) for item in response.get('Items', [])]
    
    except ClientError as e:
        print(e.response['Error']['Message'])
        return []
         

def add_recipe(meal_type: str, recipe: RecipeCreate):
    recipe_id = str(uuid4())
    Item = {
            'id': recipe_id,
            'meal_type': meal_type,
            'name': recipe.name,
            'picture':recipe.picture,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions
        }
    try:
        table.put_item(Item=item)
        return Recipe(**item)
    
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    
   