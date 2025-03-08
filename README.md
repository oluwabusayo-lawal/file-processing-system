# File Processing System

This project is a **local cloud-based file processing system** that uses **Localstack** to emulate AWS services. It processes CSV files by:
1. Uploading them to an S3 bucket.
2. Extracting metadata (row count, column count, column names).
3. Storing the metadata in a DynamoDB table.

The system is designed to be **lightweight**, **easy to set up**, and **scalable**. It demonstrates core cloud engineering skills, including working with **S3**, **Lambda**, and **DynamoDB**.

---

## Key Features
- **CSV File Upload**: Upload CSV files to an S3 bucket.
- **Metadata Extraction**: Automatically extract metadata (filename, upload timestamp, file size, row count, column count, column names).
- **Metadata Storage**: Store metadata in a DynamoDB table for easy querying and analysis.
- **Local Development**: Uses **Localstack** to emulate AWS services locally, avoiding cloud costs during development.
- **Error Handling**: Robust error handling ensures the system can handle invalid CSV files or connection issues gracefully.

---

## Technical Stack
- **Programming Language**: Python
- **AWS Services** (emulated using Localstack):
  - **S3**: For file storage.
  - **Lambda**: For processing CSV files and extracting metadata.
  - **DynamoDB**: For storing metadata.
- **Libraries**:
  - **Boto3**: AWS SDK for Python.
  - **Pandas**: For reading and processing CSV files.
- **Tools**:
  - **Docker**: For running Localstack.
  - **Git**: For version control.

---

## Project Structure
file-processing-system/
├── README.md # Project documentation
├── .gitignore # Files to ignore in Git
├── requirements.txt # Python dependencies
├── docker-compose.yml # Localstack configuration
├── src/
│ ├── lambda_function.py # Lambda function to process CSV files
│ ├── database.py # Script to create DynamoDB table
│ ├── s3_setup.py # Script to create S3 bucket and configure event triggers
├── sample_data/
│ └── example.csv # Sample CSV file for testing
└── scripts/
├── setup_localstack.sh # Script to start Localstack
└── deploy_lambda.sh # Script to deploy the Lambda function

Copy

---

## How It Works
1. **CSV File Upload**:
   - A CSV file is uploaded to the S3 bucket (`test-bucket`).
   - This triggers an S3 event notification.

2. **Lambda Function**:
   - The Lambda function (`lambda_function.py`) is automatically triggered by the S3 event.
   - It downloads the CSV file, extracts metadata, and stores it in the DynamoDB table (`MetadataTable`).

3. **Metadata Storage**:
   - The metadata is stored in DynamoDB for easy querying and analysis.

---

## Setup Instructions

### Prerequisites
1. **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).
3. **Python**: Install Python 3.8 or higher from [here](https://www.python.org/downloads/).
4. **AWS CLI**: Install the AWS CLI from [here](https://aws.amazon.com/cli/).

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
Step 5: Configure S3 Bucket and Event Trigger
Run the following script to create the S3 bucket and configure the Lambda trigger:

bash
Copy
python src/s3_setup.py
Step 6: Deploy the Lambda Function
Deploy the Lambda function using the following script:

bash
Copy
./scripts/deploy_lambda.sh
Step 7: Upload a CSV File to S3
Upload a sample CSV file to the S3 bucket:

bash
Copy
aws --endpoint-url=http://localhost:4566 s3 cp sample_data/example.csv s3://test-bucket/example.csv
Step 8: Verify the Results
Check the Lambda logs to confirm the file was processed:

bash
Copy
aws --endpoint-url=http://localhost:4566 logs tail /aws/lambda/FileProcessorLambda
Query the DynamoDB table to view the stored metadata:

bash
Copy
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name MetadataTable
Sample CSV File
The sample_data/example.csv file is provided for testing:

Copy
id,name,age,city,date
1,John,25,New York,2024-01-01
2,Jane,30,Los Angeles,2024-01-02
Expected Output from DynamoDB
After uploading the sample CSV file to S3, the Lambda function will process it and store the metadata in the DynamoDB table (MetadataTable). Here’s the expected output when you query the DynamoDB table:

json
Copy
{
  "Items": [
    {
      "filename": "example.csv",
      "upload_timestamp": "2024-03-15 10:30:45",
      "file_size_bytes": 1234,
      "row_count": 2,
      "column_count": 5,
      "column_names": ["id", "name", "age", "city", "date"]
    }
  ],
  "Count": 1,
  "ScannedCount": 1
}
Explanation of the Output
filename: The name of the uploaded CSV file.

upload_timestamp: The timestamp when the file was processed.

file_size_bytes: The size of the file in bytes.

row_count: The number of rows in the CSV file.

column_count: The number of columns in the CSV file.

column_names: A list of column names in the CSV file.

Error Handling
The system handles the following errors gracefully:

Invalid CSV Files: Logs an error if the file is not a valid CSV.

Connection Issues: Logs an error if there’s a problem connecting to S3 or DynamoDB.

Missing Files: Logs an error if the uploaded file is missing or inaccessible.

Future Improvements
Add Unit Tests: Write unit tests for the Lambda function and other components.

Support Larger Files: Optimize the system to handle larger CSV files (e.g., >10MB).

Add Notifications: Send notifications (e.g., email, Slack) when a file is processed.

Deploy to AWS: Extend the system to run on actual AWS services (S3, Lambda, DynamoDB).

References
Localstack Documentation

Boto3 Documentation

Pandas Documentation

Conclusion
This project demonstrates my ability to:

Work with AWS services (S3, Lambda, DynamoDB) using Localstack.

Write clean, modular, and maintainable code in Python.

Handle error scenarios gracefully.

Document and explain technical concepts clearly.