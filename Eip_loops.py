import boto3
client=boto3.client('ec2')
sns_client = boto3.client('sns')


eip_resp = client.describe_addresses()
unused_eips=set()
# To print Unused EIP's
for address in eip_resp["Addresses"]:
    if 'InstanceId' not in address:
        unused_eips.add(address['AllocationId'])
print(unused_eips)

# To delete Unused Eips
for allocation_id in unused_eips:
    response= client.release_address(
        AllocationId=allocation_id,
        DryRun=False
    )

# To send an alert
response = sns_client.publish(
    TopicArn='arn:aws:sns:ap-south-1:189945461814:Email_Alerts',
    Message="Unused EIP's and going to delete",
    Subject="An alert for EIP's"
)
