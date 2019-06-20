import boto3
client = boto3.client('ec2')
# To associate eip to an instance
response = client.associate_address(
    AllocationId='eipalloc-02b2f4fbaee9cd73f',
    InstanceId='i-08905207e090dff0c'
)
print(response)