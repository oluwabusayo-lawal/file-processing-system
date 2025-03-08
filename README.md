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
file-processing-system/ ├── README.md # Project documentation ├── .gitignore # Files to ignore in Git ├── requirements.txt # Python dependencies ├── docker-compose.yml # Localstack configuration ├── src/ │ ├── lambda_function.py # Lambda function to process CSV files │ ├── database.py # Script to create DynamoDB table │ ├── s3_setup.py # Script to create S3 bucket and configure event triggers ├── sample_data/ │ └── example.csv # Sample CSV file for testing └── scripts/ ├── setup_localstack.sh # Script to start Localstack └── deploy_lambda.sh # Script to deploy the Lambda function

markdown
Copy
Edit

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

## Step 2: Install Python Dependencies
Run the following command to install the Python dependencies:

```bash
pip install -r requirements.txt
