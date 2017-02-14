#!/usr/bin/env python
import boto3
import json

username='Chini'
client = boto3.client('dynamodb')
response = client.get_item( TableName='MetaData', Key={'UserName': { 'S': username}})
print response
