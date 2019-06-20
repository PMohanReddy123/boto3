import boto3
client = boto3.client('ec2')
# To create EIP
Eip = client.allocate_address(
    Domain='vpc'
)

# To associate eip to an instance
response = client.associate_address(
    AllocationId=Eip['AllocationId'],
    InstanceId='i-08905207e090dff0c'
)
# To detach from an instance
release=client.disassociate_address(
    AssociationId=response['AssociationId']
)

# To release EIPs
client.release_address(
    AllocationId=Eip['AllocationId']
)