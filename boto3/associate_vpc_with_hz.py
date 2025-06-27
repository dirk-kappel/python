"""Associate a VPC with a Private Hosted Zone in another account."""

import boto3

profile_a = ""
region_a = ""
profile_b = ""
region_b = ""
vpc_a = ""
vpc_b = ""

# Create sessions for Accounts A and B.
session_a = boto3.Session(profile_name=profile_a, region_name=region_a)
session_b = boto3.Session(profile_name=profile_b, region_name=region_b)

# Create route 53 clients for both sessions.
client_a = session_a.client("route53")
client_b = session_b.client("route53")

private_hosted_zones = []

def discover_phz():
    """Discover all of the Private Hosted Zones in Account A."""
    print(
        "-" * 10 + "Discovering vpc endpoint Private Hosted Zones in vpc:",
        vpc_a + "-" * 10,
    )
    response = client_a.list_hosted_zones_by_vpc(
        VPCId=vpc_a,
        VPCRegion=region_a,
    )
    # Set all the hosted zones for vpc endpoints and store them in a list.
    for hosted_zone in response["HostedZoneSummaries"]:
        if hosted_zone["Name"].endswith(region_a + ".amazonaws.com."):
            print(hosted_zone)
            private_hosted_zones.append(hosted_zone["HostedZoneId"])
    return private_hosted_zones

def create_authorization(private_hosted_zones):
    """
    Create the vpc association authorization from Account A.

    Args:
        private_hosted_zones (list): List of private hosted zones to authorize.

    """
    print(
        "-" * 10 + "Creating authorization for",
        vpc_a,
        "to associate Private Hosted Zones with",
        vpc_b + "-" * 10,
    )
    for private_hosted_zone in private_hosted_zones:
        print("Authorizing the association of", private_hosted_zone, "for", vpc_b)
        client_a.create_vpc_association_authorization(
            HostedZoneId=private_hosted_zone,
            VPC={
                "VPCRegion": region_b,
                "VPCId": vpc_b,
            },
        )

def associate_phz(private_hosted_zones):
    """
    Associate the vpc with the private hosted zone to Account B.

    Args:
        private_hosted_zones (list): List of private hosted zones to associate.

    """
    print("-" * 10 + "Begin association of Private Hosted Zones with", vpc_b + "-" * 10)
    for private_hosted_zone in private_hosted_zones:
        print("Associating", private_hosted_zone, "with", vpc_b)
        client_b.associate_vpc_with_hosted_zone(
            HostedZoneId=private_hosted_zone,
            VPC={
                "VPCRegion": region_b,
                "VPCId": vpc_b,
            },
        )

def delete_authorization(private_hosted_zones):
    """
    Delete the vpc association authorization from Account A.

    Args:
        private_hosted_zones (list): List of private hosted zones to delete authorization.

    """
    print(
        "-" * 10 + "Deleting authorization for",
        vpc_a,
        "to associate Private Hosted Zones with",
        vpc_b + "-" * 10,
    )
    for private_hosted_zone in private_hosted_zones:
        print("Deleting authorization of", private_hosted_zone, "for", vpc_b)
        client_a.delete_vpc_association_authorization(
            HostedZoneId=private_hosted_zone,
            VPC={
                "VPCRegion": region_b,
                "VPCId": vpc_b,
            },
        )


if __name__ == "__main__":
    print()
    discover_phz()
    print()
    create_authorization(private_hosted_zones)
    print()
    associate_phz(private_hosted_zones)
    print()
    delete_authorization(private_hosted_zones)
    print()
    print("Association Completed!")
    print()
