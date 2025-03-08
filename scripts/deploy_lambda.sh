#!/bin/bash

# Zip the Lambda function
zip -r lambda_function.zip src/lambda_function.py

# Deploy to LocalStack
aws --endpoint-url=http://localhost:4566 lambda create-function \
    --function-name FileProcessorLambda \
    --runtime python3.8 \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda_function.zip
