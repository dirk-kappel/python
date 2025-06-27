import boto3

# Specify the profile name for the default session
boto3.setup_default_session(profile_name="", region_name="us-east-1")

# The Client call will return information about the job that was just completed
ec2client = boto3.client("ec2")
ec2resource=boto3.resource("ec2")

# Get all of the network ACLs
response=ec2client.describe_network_acls()

# Enter it into a Service Resource object
nacl=ec2resource.NetworkAcl("acl-0c5d711309e46c473")

# Create an entry. Egress=False means this is an inbound rule
nacl.create_entry(RuleNumber=50, Protocol="-1", RuleAction="deny", Egress=False, CidrBlock="1.2.3.4/24")

# Block all outbound traffic on port 22
nacl.create_entry(RuleNumber=3000, Protocol="6", RuleAction="deny", Egress=True, CidrBlock="0.0.0.0/0", PortRange={"From":22,"To":22})
