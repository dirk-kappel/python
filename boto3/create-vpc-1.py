import boto3

# Specify the profile name for the default session
boto3.setup_default_session(profile_name="", region_name="us-east-1")

# The Client call will return information about the job that was just completed
ec2client = boto3.client("ec2")

response = ec2client.create_vpc(CidrBlock="10.100.0.0/16")

# This is the info returned in the response
print("This is the info returned in the response")
print(response)

# The response is a dictionary with 1 key, 'VPC', which holds all the details of the new VPC
print("The response is a dictionary with 1 key, 'VPC', which holds all the details of the new VPC")
print(response["Vpc"])

# The each item in the dict can be referenced by the key
print("The each item in the dict can be referenced by the key")
print(response["Vpc"]["VpcId"])
