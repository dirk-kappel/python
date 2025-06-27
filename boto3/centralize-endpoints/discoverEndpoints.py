import boto3

profile=""
region="us-east-1"

# Specify the profile name for the default session
# You may need to log in first with your mfa.
boto3.setup_default_session(profile_name=profile, region_name=region)

ec2client = boto3.client("ec2")

endpoints = {}

# Get all the endpoints in the account.
def get_endpoints():
    response = ec2client.describe_vpc_endpoints()
    for vpc_endpoint in response["VpcEndpoints"]:
        if vpc_endpoint["VpcEndpointType"] == "Gateway":
            continue
        endpoints[vpc_endpoint["ServiceName"]] = {"VpcEndpointId":vpc_endpoint["VpcEndpointId"],"VpcEndpointType":vpc_endpoint["VpcEndpointType"], "NetworkInterfaceIds":vpc_endpoint["NetworkInterfaceIds"], "VpcId":vpc_endpoint["VpcId"]}
        # Clean the DNS name by reverse the order of the service name.
        service_name = vpc_endpoint["ServiceName"]
        service_name_list = service_name.split(".")
        service_name_list.reverse()
        endpoints[vpc_endpoint["ServiceName"]]["DnsName"] = ".".join(service_name_list)

# Get the ip addresses for the network interfaces for each endpoint.
def get_endpoint_ips():
    for endpoint_service in endpoints:
        endpoints[endpoint_service]["NetworkInterfaceIP"]=[]
        for network_interface in endpoints[endpoint_service]["NetworkInterfaceIds"]:
            describe_network_interface = ec2client.describe_network_interfaces(NetworkInterfaceIds=[network_interface])
            endpoints[endpoint_service]["NetworkInterfaceIP"].append(describe_network_interface["NetworkInterfaces"][0]["PrivateIpAddresses"][0]["PrivateIpAddress"])

def main():
    get_endpoints()
    get_endpoint_ips()
    return endpoints

if __name__=="__main__":
    get_endpoints()
    get_endpoint_ips()
    for endpoint in endpoints:
        print(endpoints[endpoint]["DnsName"], endpoints[endpoint]["VpcId"])

# for endpoint in endpoints:
#     print(endpoints[endpoint]['DnsName'])
#     print(endpoints[endpoint]['NetworkInterfaceIP'])
