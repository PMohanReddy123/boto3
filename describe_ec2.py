import boto3
# Describe Instances
client = boto3.client('ec2')
response = client.describe_instances()
for response in response['Reservations']:
    for instance in response['Instances']:
        InstanceId=instance['InstanceId']
print(InstanceId)