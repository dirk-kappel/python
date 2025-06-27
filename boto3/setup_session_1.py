"""Creates a session with a specific profile name."""

import boto3

# ------------ Variables ------------
profile = ""  # The profile name to use for the session.

# Setup a session using the specified profile.
boto3.setup_default_session(profile_name=profile)

s3=boto3.client("s3")

response = s3.list_buckets()

# Print the names of the buckets from the response.
for bucket in response["Buckets"]:
    print(f"{bucket["Name"]}")
