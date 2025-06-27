import json

import boto3

# Input profile name
# profile_name = input("Enter AWS profile name: ")
profile_name = ""

# Create a new session using the specified AWS profile
session = boto3.Session(profile_name=profile_name)

# Initialize Boto3 EC2 client
ec2_client = session.client("ec2", region_name="us-east-1")

# Function to get security group details
def get_security_group_details(security_group_id):
    response = ec2_client.describe_security_groups(GroupIds=[security_group_id])
    security_group = response["SecurityGroups"][0]
    print(json.dumps(security_group, indent=4, default=str))
    return {
        "name": security_group["GroupName"],
        "description": security_group["Description"],
        "ingress_rules": security_group["IpPermissions"],
        "egress_rules": security_group["IpPermissionsEgress"],
        "tags": security_group["Tags"],
    }

# security_groups = get_security_group_details('sg-0ee411d860b4aa5c5')

# Function to print security group details in JSON-like format
def print_security_group_details(group_details):
        print(f"name          = \"{group_details['name']}\"")
        print(f"description   = \"{group_details['description']}\"")

        def print_rule(rule_set):
            print(f"  {rule_set} =", "{")
            count=0
            for rule in group_details[rule_set]:
                # def a function.
                def create_each_rule(rule, ip_range, sec_grp_id):
                    nonlocal count
                    count+=1
                    print(f"  rule_{count} =","{")
                    if ip_range:
                        print(f"    cidr_ipv4   = \"{ip_range['CidrIp']}\"")
                        if ip_range.get("Description"):
                          print(f"    description = \"{ip_range['Description']}\"")
                        else:
                          print('    description = ""')
                    if sec_grp_id:
                        print(f'    referenced_security_group_id = "{sec_grp_id}"')
                        if sec_grp_id.get("Description"):
                          print(f"    description = \"{sec_grp_id['Description']}\"")
                        else:
                          print('    description = ""')
                    if rule.get("FromPort") != None:
                        print(f"    from_port   = {rule['FromPort']}")
                    else:
                        print("    from_port   = -1")
                    print(f"    ip_protocol = \"{rule['IpProtocol']}\"")
                    if rule.get("ToPort"):
                        print(f"    to_port     = {rule['ToPort']}")
                    else:
                        print("    to_port     = -1")
                    if count < len(group_details[rule_set]):
                        print("    },")
                    else:
                        print("    }")

                # If using cidr ips
                if rule.get("IpRanges"):
                    for ip_range in rule["IpRanges"]:
                        create_each_rule(rule, ip_range=ip_range, sec_grp_id=None)

                # If using sec group references
                if rule.get("UserIdGroupPairs"):
                    for sec_grp_id in rule["UserIdGroupPairs"]:
                        create_each_rule(rule, cidr_ip=None, sec_grp_id=sec_grp_id)

            print("  }")
        print_rule("ingress_rules")
        print_rule("egress_rules")
        print("}")


# Dictionary to store security group details
security_group_id = "sg-0ee411d860b4aa5c5"
security_groups = {}

security_groups[security_group_id] = get_security_group_details(security_group_id)

print(security_groups)
# Iterate security group details
for group_id, group_details in security_groups.items():
    print_security_group_details(group_details)












# tag_value = ""
# for tag in returned_values['tags']:
#     if tag['Key'] == 'Name':
#         tag_value = tag['Value']
#         break
# print(tag_value)
