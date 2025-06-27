"""Creates a terraform configuration based on the existing rules of a given security group."""

from pathlib import Path

import boto3

# Input profile name
# profile_name = input("Enter AWS profile name: ")
profile_name = ""

# Create a new session using the specified AWS profile
session = boto3.Session(profile_name=profile_name)

# Initialize Boto3 EC2 client
ec2_client = session.client("ec2", region_name="us-gov-west-1")

# Function to get security group details
def get_security_group_details(security_group_id):
    response = ec2_client.describe_security_groups(GroupIds=[security_group_id])
    security_group = response["SecurityGroups"][0]
    if security_group.get("Tags") is None:
        security_group["Tags"] = ""
    return {
        "name": security_group["GroupName"],
        "description": security_group["Description"],
        "ingress_rules": security_group["IpPermissions"],
        "egress_rules": security_group["IpPermissionsEgress"],
        "tags": security_group["Tags"],
    }

# Function to print security group details in JSON-like format
def sg_details(group_details,output_file_path):
    output_file_path = Path(f"{output_file_path}.tf")
    with Path(output_file_path).open("w") as output_file:
        # print(output_file_path,"= {", file=output_file)
        # print("security_groups = {", file=output_file)
        print("  default = {", file=output_file)
        print(f"    name          = \"{group_details['name']}\"", file=output_file)
        print(f"    description   = \"{group_details['description']}\"", file=output_file)

        def print_rule(rule_set):
            print(f"    {rule_set} =", "{", file=output_file)
            count=0
            for rule in group_details[rule_set]:
                # def a function.
                def create_each_rule(rule, cidr_ip, sec_grp_id):
                    nonlocal count
                    count+=1
                    print(f"      rule_{count} =","{", file=output_file)
                    if cidr_ip:
                        print(f'        cidr_ipv4   = "{cidr_ip}"', file=output_file)
                    if sec_grp_id:
                        print(f'        referenced_security_group_id = "{sec_grp_id}"', file=output_file)
                    if rule.get("Description"):
                        print(f"        description = {rule['Description']}", file=output_file)
                    else:
                        print('        description = ""', file=output_file)
                    if rule.get("FromPort") != None:
                        print(f"        from_port   = {rule['FromPort']}", file=output_file)
                    else:
                        print("        from_port   = -1", file=output_file)
                    print(f"        ip_protocol = \"{rule['IpProtocol']}\"", file=output_file)
                    if rule.get("ToPort"):
                        print(f"        to_port     = {rule['ToPort']}", file=output_file)
                    else:
                        print("        to_port     = -1", file=output_file)
                    if count < len(group_details[rule_set]):
                        print("      },", file=output_file)
                    else:
                        print("      }", file=output_file)

                # If using cidr ips
                if rule.get("IpRanges"):
                    cidr_ips = [ip_range["CidrIp"] for ip_range in rule["IpRanges"]]
                    for cidr_ip in cidr_ips:
                        create_each_rule(rule, cidr_ip=cidr_ip, sec_grp_id=None)
                # If using sec group references
                if rule.get("UserIdGroupPairs"):
                    referenced_security_group_id=[sec_grp["GroupId"] for sec_grp in rule["UserIdGroupPairs"]]
                    for sec_grp_id in referenced_security_group_id:
                        create_each_rule(rule, cidr_ip=None, sec_grp_id=sec_grp_id)

            print("    }", file=output_file)
        print_rule("ingress_rules")
        print_rule("egress_rules")
        # print("  }", file=output_file)
        # print("}", file=output_file)

        tag_name_value = ""
        for tag in group_details["tags"]:
            if tag["Key"] == "Name":
                tag_name_value = tag["Value"]
                break
        print("    tags =","{", file=output_file)
        print(f'      Name = "{tag_name_value}"', file=output_file)
        print("    }", file=output_file)
        # print(f"vpc_id = \"{vpc_id}\"", file=output_file)
        print("  }", file=output_file)

# Read non-empty network interfaces list from file
non_empty_network_interfaces = []

# Input the VPC ID
vpc_id = input("Enter VPC ID: ")

# File path with the prefix based on the VPC ID
file_path = Path(f"{vpc_id}_non_empty_ENI.txt")

with Path(file_path).open("r") as file:
    for line in file:
        non_empty_network_interfaces.append({"SecurityGroupId": line.strip()})

# Dictionary to store security group details
security_groups = {}

# Iterate through non-empty network interfaces
for interface in non_empty_network_interfaces:
    security_group_id = interface["SecurityGroupId"]
    security_groups[security_group_id] = get_security_group_details(security_group_id)

# Iterate through non-empty network interfaces
for group_id, group_details in security_groups.items():
    sg_details(group_details,group_id)
