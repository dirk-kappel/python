import boto3

ec2client=boto3.client("ec2")
ec2resource=boto3.resource("ec2")

# Create an internet gateway using client
response=ec2client.create_internet_gateway()

# Store the Id in a variable
newigid=response["InternetGateway"]["InternetGatewayId"]

# Create a resource out of the Internet Gateway
newigw=ec2resource.InternetGateway(newigid)

# Create an internet gateway using EC2 Service Resource
igw_object=ec2resource.create_internet_gateway()

# Add a tag to the internet gateway object that was just created
response=igw_object.create_tags(Tags=[{"Key":"Name","Value":"IGW_OBJECT"}])

# Create tags using the client
response=ec2client.create_tags(Resources=[newigw.id], Tags=[{"Key":"Name","Value":"CREATED_FROM_CLIENT"}])

# Attach using VPC action
vpc.attach_internet_gateway(InternetGatewayId=newigid)
# Detach the IGW using VPC action
vpc.detach_internet_gateway(InternetGatewayId=newigid)

# Attach using EC2 Client
ec2client.attach_internet_gateway(InternetGatewayId=newigid, VpcId=vpc.id)
# Detach the IGW using EC2 Client
ec2client.detach_internet_gateway(InternetGatewayId=newigid, VpcId=vpc.id)

# Attach using IGW action
igw_object.attach_to_vpc(VpcId=vpc.id)
# Dettach using IGW action
igw_object.detach_from_vpc(VpcId=vpc.id)

# Describe all internet gateways using the Client method
igw_response=ec2client.describe_internet_gateways()

# Place an existing internet gateway into a Service Resource
igw=ec2resource.InternetGateway(ec2client.describe_internet_gateways(Filters=[{"Name":"attachment.vpc-id","Values":[vpc_1.id]}])["InternetGateways"][0]["InternetGatewayId"])

