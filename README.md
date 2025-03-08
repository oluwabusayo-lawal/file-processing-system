markdown
Copy
# File Processing System

This project processes CSV files using a local AWS cloud stack emulator (Localstack). It uploads CSV files to an S3 bucket, extracts metadata (row count, column count, column names), and stores the metadata in a DynamoDB table.

## Features
- **CSV Upload**: Upload CSV files to an S3 bucket.
- **Metadata Extraction**: Extract metadata such as row count, column count, and column names.
- **Metadata Storage**: Store metadata in a DynamoDB table.
- **Local Development**: Uses Localstack to emulate AWS services locally.

## Setup Instructions

### Prerequisites
1. **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).
3. **Python**: Install Python 3.8 or higher from [here](https://www.python.org/downloads/).

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/file-processing-system.git
cd file-processing-system
Step 2: Install Python Dependencies
bash
Copy
pip install -r requirements.txt
Step 3: Start Localstack
Run the following script to start Localstack using Docker Compose:

bash
Copy
./scripts/setup_localstack.sh
Step 4: Create the DynamoDB Table
Run the following script to create the DynamoDB table:

bash
Copy
python src/database.py
Step 5: Upload a CSV File to S3
Upload a sample CSV file to the S3 bucket:

bash
Copy
aws --endpoint-url=http://localhost:4566 s3 cp sample_data/example.csv s3://test-bucket/example.csv
Step 6: Deploy the Lambda Function
Deploy the Lambda function using the following script:

bash
Copy
./scripts/deploy_lambda.sh
Step 7: Test the System
The Lambda function will automatically process the uploaded CSV file and store the metadata in the DynamoDB table. You can verify the metadata by querying the DynamoDB table:

bash
Copy
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name MetadataTable
Project Structure
Copy
file-processing-system/
├── README.md
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── src/
│   ├── lambda_function.py
│   ├── database.py
│   └── s3_setup.py
├── sample_data/
│   └── example.csv
└── scripts/
    ├── setup_localstack.sh
    └── deploy_lambda.sh
Key Files
lambda_function.py: Contains the Lambda function to process CSV files and extract metadata.

database.py: Creates the DynamoDB table for storing metadata.

s3_setup.py: Creates the S3 bucket for storing CSV files.

setup_localstack.sh: Starts Localstack using Docker Compose.

deploy_lambda.sh: Deploys the Lambda function to Localstack.

Sample CSV File
The sample_data/example.csv file is provided for testing:

Copy
id,name,age,city,date
1,John,25,New York,2024-01-01
2,Jane,30,Los Angeles,2024-01-02
Troubleshooting
Localstack Not Starting: Ensure Docker is running and try restarting Localstack.

Lambda Function Not Triggering: Verify that the S3 bucket and DynamoDB table were created successfully.

Invalid CSV File: Ensure the CSV file is properly formatted.

References
Localstack Documentation

Boto3 Documentation

Pandas Documentation

