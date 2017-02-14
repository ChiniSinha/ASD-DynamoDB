#!/usr/bin/env python
import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('MetaData')
global users
with open("data.json") as json_file:
	users = json.load(json_file)
	print users
	
	username = users['UserName']
	lastname = users['LastName']
	major = users['Major']
	print ("Adding user: ", username, " ", lastname, " ", major)
	table.put_item(Item={'UserName': username, 'LastName': lastname, 'Major': major})

