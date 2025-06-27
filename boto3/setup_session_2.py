"""Create a session with the default profile (or environment variables), then list S3 buckets."""

import boto3

# Create a session using the default profile
s3=boto3.client("s3")

response = s3.list_buckets()

# Print the names of the buckets from the response.
for bucket in response["Buckets"]:
    print(f"{bucket["Name"]}")
