import boto3
import json

def lambda_handler(event, context):
    # Perform CI/CD actions here (e.g., deploy code, run tests)
    
    response = {
        'statusCode': 200,
        'body': json.dumps('CI/CD Lambda executed successfully!')
    }
    return response
