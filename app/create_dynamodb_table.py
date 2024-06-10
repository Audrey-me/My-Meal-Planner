import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def create_recipe_table():
    table = dynamodb.create_table(
        TableName='Recipes',
        KeySchema=[
            {
                'AttributeName': 'meal_type',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'meal_type',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    table.meta.client.get_waiter('table_exists').wait(TableName='Recipes')
    print(f"Table status: {table.table_status}")

if __name__ == "__main__":
    create_recipe_table()
