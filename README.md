<<<<<<< HEAD
# AWS Lambda Secrets Manager Example

This project demonstrates how to fetch secrets securely from AWS Secrets Manager using AWS Lambda and Python.

## Services Used

- AWS Lambda
- AWS Secrets Manager
- IAM
- Python boto3 SDK

## Project Structure

```bash
get-secret-function/
│
├── lambda_function.py
├── requirements.txt
└── README.md
```

## Lambda Function

The Lambda function retrieves secrets from AWS Secrets Manager.

## Setup

1. Create a secret in AWS Secrets Manager
2. Create Lambda function
3. Attach IAM permission:
   - SecretsManagerReadWrite
4. Deploy code
5. Test Lambda

## Example Response

```json
{
  "statusCode": 200,
  "body": {
    "message": "Secret fetched successfully"
  }
}
```

## Author

Srini Reddy
=======
# aws-lambda-secrets-manager
AWS Lambda project using AWS Secrets Manager and Python
>>>>>>> b90d04f0b142fc03f4cb64fb308a0f4db7caafa0
