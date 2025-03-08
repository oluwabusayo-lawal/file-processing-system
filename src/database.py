import boto3

# DynamoDB Setup
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')

def create_metadata_table():
    try:
        table = dynamodb.create_table(
            TableName='MetadataTable',
            KeySchema=[{'AttributeName': 'filename', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'filename', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        table.wait_until_exists()
        print("Metadata table created.")
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        print("Table already exists.")

if __name__ == "__main__":
    create_metadata_table()
