# This creates a script to get all Security Groups in a VPC and check if they are attached to any Network Interfaces.
# The script will output two files: one with Security Group IDs that are not attached to any Network Interfaces and one with Security Group IDs that are attached to Network Interfaces.

from pathlib import Path

import boto3

# Input profile name
region_name = "us-east-1"

# Create a new session using the AWS Management Console profile
session = boto3.Session()

# Initialize Boto3 EC2 client
ec2_client = session.client("ec2", region_name)

# Input VPC ID as the first argument
VPC_ID = input("Enter VPC ID: ")

# Define output files
output_file_empty = Path(f"{VPC_ID}_empty_ENI.txt")
output_file_non_empty = Path(f"{VPC_ID}_non_empty_ENI.txt")

# Clear previous output files
Path.open(output_file_empty, "w").close()
Path.open(output_file_non_empty, "w").close()

# Get all Security Group IDs in a VPC
response = ec2_client.describe_security_groups(
    Filters=[
        {
            "Name": "vpc-id",
            "Values": [VPC_ID],
        },
    ],
)

sec_group_ids = [group["GroupId"] for group in response["SecurityGroups"]]

# Get total number of Security Group IDs
total_sec_group_ids = len(sec_group_ids)

# Iterate one by one and get the details
for i, sec_group_id in enumerate(sec_group_ids):
    # Print progress to console
    print(
        f"Checking Security Group ID: {sec_group_id} ({i + 1} of {total_sec_group_ids})",
    )

    # Get Network Interfaces for the current Security Group
    response = ec2_client.describe_network_interfaces(
        Filters=[
            {
                "Name": "group-id",
                "Values": [sec_group_id],
            },
        ],
    )

    network_interfaces = response["NetworkInterfaces"]

    # Check if NetworkInterfaces array is empty
    if not network_interfaces:
        with Path.open(output_file_empty, "a") as file:
            file.write(sec_group_id + "\n")
    else:
        with Path.open(output_file_non_empty, "a") as file:
            file.write(sec_group_id + "\n")

print(f"Results have been saved to {output_file_empty} and {output_file_non_empty}.")
