import json
import boto3

s3Client = boto3.client('s3')

def lambda_handler(event, context):
    
    print(event)

    #get bucket from event JSON
    s3Bucket = event['Records'][0]['s3']['bucket']['name']
    bucketKey = event['Records'][0]['s3']['object']['key']
    #bucketKey = "movies.txt"
    data = s3Client.get_object(Bucket=s3Bucket, Key=bucketKey)
    #here you can place try catch for exceptions
    fileContent = data["Body"].read().decode("utf-8")

    print(fileContent)
