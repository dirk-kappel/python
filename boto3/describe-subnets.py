import boto3

# Specify the profile name for the default session
boto3.setup_default_session(profile_name="")

ec2client = boto3.client("ec2")

# List all the subnets in the default region of the given profile
all_subnets=ec2client.describe_subnets()

# Loop through all of the subnets
for each_subnet in all_subnets["Subnets"]:
    print(each_subnet)

# Use a filter to describe the subnets
all_subnets=ec2client.describe_subnets(Filters=[{"Name":"cidrBlock", "Values":["10.100.1.0/24","10.100.2.0/24","10.100.3.0/24"]}])

for each_subnet in all_subnets["Subnets"]:
    print(each_subnet)
