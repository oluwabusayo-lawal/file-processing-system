import boto3
import pandas as pd
from datetime import datetime

# AWS Clients
s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
table = dynamodb.Table('MetadataTable')

def lambda_handler(event, context):
    try:
        # Get file details
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        # Read CSV
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        df = pd.read_csv(response['Body'])

        # Extract Metadata
        metadata = {
            'filename': file_key,
            'upload_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'file_size_bytes': df.memory_usage(index=True, deep=True).sum(),
            'row_count': len(df),
            'column_count': len(df.columns),
            'column_names': list(df.columns)
        }

        # Store in DynamoDB
        table.put_item(Item=metadata)

        print(f"Metadata stored: {metadata}")
        return {'statusCode': 200, 'body': metadata}
    except Exception as e:
        print(f"Error: {e}")
        return {'statusCode': 500, 'body': str(e)}
