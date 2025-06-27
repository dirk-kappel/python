import boto3

ec2client=boto3.client("ec2")
ec2resource=boto3.resource("ec2")

# Allocate an EIP
newaddr=ec2client.allocate_address()

# Put EIP into a resource object
eip=ec2resource.VpcAddress(newaddr["AllocationId"])

# Release EIP
eip.release()
