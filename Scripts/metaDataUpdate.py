#!/usr/bin/env python
import boto3
import json

username='Chini'
major='CS'
client = boto3.client('dynamodb')
client.update_item( TableName='MetaData', Key={'UserName': { 'S': username}}, AttributeUpdates={'Major': {'Value': {'S': major}}})

