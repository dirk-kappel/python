"""Empty and delete an S3 bucket."""

import json

import boto3

boto3.setup_default_session(profile_name="")
s3resource=boto3.resource("s3")

# Request input for the bucket name
bucket_name=input("Bucket Name: ")

# Empty the objects from the bucket
s3resource.Bucket(bucket_name).objects.all().delete()

# Delete the bucket
response=s3resource.Bucket(bucket_name).delete()

# Print to screen the json response from the delete action
json_object=json.dumps(response, indent=4)
print(json_object)
