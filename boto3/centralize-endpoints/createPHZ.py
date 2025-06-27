from datetime import datetime

import boto3

profile=""
region="us-east-1"

# Specify the profile name for the default session
# You may need to log in first with your mfa.
boto3.setup_default_session(profile_name=profile, region_name=region)

client = boto3.client("route53")

privateHostedZones = {}

# Create a Private Hosted Zone for each endpoint.
def create_phz(endpoints):
    print("Creating Private Hosted Zones...")
    for endpoint in endpoints:
        response = client.create_hosted_zone(Name=endpoints[endpoint]["DnsName"], VPC={"VPCRegion":region,"VPCId":endpoints[endpoint]["VpcId"]}, CallerReference=datetime.now().strftime("%m/%d/%Y:%H:%M:%S.%f"), HostedZoneConfig={"Comment": "VPC Endpoint", "PrivateZone":True})
        # privateHostedZones[endpoints[endpoint]['DnsName']] = response['HostedZone']['Id'].lstrip('/hostedzone/')
        print("Created:", endpoints[endpoint]["DnsName"], "Hosted Zone Id:", "-----", response["HostedZone"]["Id"].lstrip("/hostedzone/"))
        endpoints[endpoint]["HostedZoneId"] = response["HostedZone"]["Id"].lstrip("/hostedzone/")
    return endpoints

def create_record(endpoints):
    print("Creating A Records...")
    for endpoint in endpoints:
        client.change_resource_record_sets(HostedZoneId=endpoints[endpoint]["HostedZoneId"], ChangeBatch={
            "Changes":[
                {
                    "Action":"CREATE",
                    "ResourceRecordSet": {
                        "Name":endpoints[endpoint]["DnsName"],
                        "Type":"A",
                        "TTL":60,
                        "ResourceRecords": [
                            {
                                "Value":endpoints[endpoint]["NetworkInterfaceIP"][0],
                            },
                        ],
                    },
                },
            ],
            "Comment":"VPC Endpoint",
        })
        print('"A" Record created for',endpoints[endpoint]["DnsName"],":",endpoints[endpoint]["NetworkInterfaceIP"][0])

def main(endpoints):
    endpoints = create_phz(endpoints)
    print()
    create_record(endpoints)
    return endpoints

if __name__=="__main__":
    phz = create_phz()
    print(phz)
