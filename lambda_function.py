import json
import boto3
from boto3.dynamodb.conditions import Key

def addBook(book):

    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('books')
    
    table.put_item(Item=book)

def lambda_handler(event, context):
    print(event)
    
    addBook(event)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }