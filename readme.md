# My Meal Planner API

It demonstrates how to build a robust API using FastAPI and store data in AWS DynamoDB. The API provides different recipe ideas for breakfast, lunch, and dinner, and includes features for adding and retrieving recipes.

## Steps to Follow

1. Create a virtual environment
    ```bash
   python3 -m venv myapienv
   source myapienv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

2. Install all the requirements by running this command
```bash
pip install -r requirements.txt
```

3. Set Up AWS Credentials to allow access to AWS Dynamodb, Provide your AWS Access Key ID, Secret Access Key, default region name, and output format when prompted.
 ```bash
   aws configure
   ```

4. Create DynamoDB Table
You can create a DynamoDB table using the AWS Management Console or by runniing this script to create the table:
```bash
   chmod 700 create_dynamodb_table.py
   python3 create_dynamodb_table.py
   ```

5. Run the Project
```bash
   python3 main.py
```

6. Sample on how to add a sample recipe
```bash
curl -X 'POST' \
 'http://127.0.0.1:8000/recipes/breakfast' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "id": "1",
 "name": "Pancakes",
 "picture": "http://example.com/pancakes.jpg",
 "ingredients": ["Flour", "Eggs", "Milk", "Sugar"],
 "instructions": ["Mix all ingredients", "Cook on a hot griddle"]
```

7. sample on how to retrieve from the database
```bash
  curl -X 'GET' \
 'http://127.0.0.1:8000/recipes/breakfast' \
 -H 'accept: application/json'
```

