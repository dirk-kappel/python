import boto3

# Specify the profile name for the default session
boto3.setup_default_session(profile_name="", region_name="us-east-1")

# The Client call will return information about the job that was just completed
ec2client = boto3.client("ec2")

# Create the service resource
ec2resource=boto3.resource("ec2")

response = ec2client.create_vpc(CidrBlock="10.100.0.0/16")

# This is the info returned in the response
print("This is the info returned in the response")
print(response)

# The response is a dictionary with 1 key, 'VPC', which holds all the details of the new VPC
print("The response is a dictionary with 1 key, 'VPC', which holds all the details of the new VPC")
newvpc=response["Vpc"]
print(newvpc)

# The each item in the dict can be referenced by the key
print("The each item in the dict can be referenced by the key")
newvpcid=response["Vpc"]["VpcId"]
print(newvpcid)

# Create a subnet for the vpc using the client
response=ec2client.create_subnet(VpcId=newvpcid, CidrBlock="10.100.1.0/24", AvailabilityZone="us-east-1a")
print(response)

# Extract the subnet id
newsubnetid=response["Subnet"]["SubnetId"]
print(newsubnetid)

# Place the subnet into an object
newsubnet=ec2resource.Subnet(newsubnetid)
print(newsubnet)

# Create a subnet for the vpc using the resource
response=ec2resource.create_subnet(VpcId=newvpcid, CidrBlock="10.100.2.0/24", AvailabilityZone="us-east-1b")
print(response)

# Extract subnet 2 id
subnet2id=response.id
print(subnet2id)

# Make to vpc an object
vpc=ec2resource.Vpc(newvpcid)
print(vpc)

# Create a subnet using the vpc object
subnet3=vpc.create_subnet(AvailabilityZone="us-east-1c", CidrBlock="10.100.3.0/24")
print(subnet3)
