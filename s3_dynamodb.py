import boto3

client_s3 = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')

S3_resp = client_s3.get_object(
    Bucket='mohanmmmmmddddd',
    Key='mohan.csv'
)

CSV_File=S3_resp['Body'].read().decode('utf-8')
employees=CSV_File.split('\r\n')
for emp in employees:
    emp=emp.split(',')
    print(emp)
    table.put_item(
        Item={
            'emp_id':emp[0],
            "name":emp[1],
            "loaction":emp[2],
            "salary":emp[3]
        }
    )

