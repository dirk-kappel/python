import boto3

# Specify the profile name for the default session
boto3.setup_default_session(profile_name="", region_name="us-east-1")

# The Client call will return information about the job that was just completed
ec2client = boto3.client("ec2")
ec2resource=boto3.resource("ec2")

# Create a new vpc or add existing to the service resource
vpc_1=ec2resource.Vpc("vpc-00af234285cc86596")

# Set variables
mysubnetid=vpc_1_subnets["Subnets"][0]["SubnetId"]
myallocid=eip.allocation_id

# Create the NAT Gateway
response=ec2client.create_nat_gateway(SubnetId=mysubnetid, AllocationId=myallocid)
