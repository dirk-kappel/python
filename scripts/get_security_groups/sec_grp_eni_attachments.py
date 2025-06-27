"""Return all of the network interfaces that a list of security groups are attached to."""

from pathlib import Path

import boto3

# Input profile name
region_name = "us-east-1"

# Create a new session using the AWS Management Console profile
session = boto3.Session()

# Initialize Boto3 EC2 client
ec2_client = session.client("ec2", region_name)

# Input the VPC ID
vpc_id = input("Enter VPC ID: ")

# File path with the prefix based on the VPC ID
file_path = Path(f"{vpc_id}_non_empty_ENI.txt")

# Initialize dictionaries and lists
sec_group_to_eni = {}
sec_group_ids = []

# Open the file with the security group ids
with Path(file_path).open("r") as file:
    for line in file:
        sec_group_ids.append(line.strip())

# Iterate one by one and get the details
for sec_group_id in sec_group_ids:
    network_interface_ids = []
    # Get Network Interfaces for the current Security Group
    response = ec2_client.describe_network_interfaces(
        Filters=[
            {
                "Name": "group-id",
                "Values": [sec_group_id],
            },
        ],
    )["NetworkInterfaces"]

    for item in response:
        # Get the value of "NetworkInterfaceId" key and append it to the list
        network_interface_ids.append(item["NetworkInterfaceId"])

    sec_group_to_eni[sec_group_id] = network_interface_ids

print(sec_group_to_eni)
