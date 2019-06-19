import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')

s3_response = s3_client.get_object(
    Bucket='mohanmmmmmddddd',
    Key='mohan.json'
)
json_s3=s3_response['Body'].read().decode('utf-8')
employees = json.loads(json_s3)
for emp in employees:
    print(emp)
    table.put_item(
        Item={
            "emp_id" :int(emp["emp_id"]),
            'name':emp['name'],
            'location':emp['location'],
            'salary':emp['salary']
        }
    )