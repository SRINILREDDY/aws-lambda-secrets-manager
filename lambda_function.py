import json
import boto3
from botocore.exceptions import ClientError


def get_secret(secret_name):

    client = boto3.client(
        "secretsmanager",
        region_name="ap-south-1"
    )

    try:

        response = client.get_secret_value(
            SecretId=secret_name
        )

        secret = response["SecretString"]

        return json.loads(secret)

    except ClientError as e:

        print("ERROR:", e)
        raise e


def lambda_handler(event, context):

    secret_name = "Snoops"

    secret = get_secret(secret_name)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Secret fetched successfully",
            "secret": secret
        })
    }