#!/bin/bash

: '
This creates a script to get all Security Groups in a VPC and check if they have any Network Interfaces attached to them.
'

# Input vpc-id as the first argument
VPC_ID=$1

# Declare arrays
declare -a EMPTY_INTERFACES
declare -a NON_EMPTY_INTERFACES

# Define output file
OUTPUT_FILE_EMPTY="empty_network_interfaces_results.txt"
OUTPUT_FILE_NON_EMPTY="non_empty_network_interfaces_results.txt"

# Clear previous output file
> "$OUTPUT_FILE_EMPTY"
> "$OUTPUT_FILE_NON_EMPTY"

# Get all Security Group Ids in a VPC
SEC_GROUP_IDS=`aws ec2 describe-security-groups --filters Name=vpc-id,Values=$VPC_ID --region us-gov-west-1 --output json --profile oldcc.management | jq -r '.SecurityGroups[] | .GroupId'`

# Get total number of Security Group IDs
TOTAL_SEC_GROUP_IDS=$(echo "$SEC_GROUP_IDS" | wc -l)

# Initialize counter
COUNT=0

# Iterate one by one and get the details
for SEC_GROUP_ID in $SEC_GROUP_IDS
do
  # Increment counter
  ((COUNT++))

  # Print progress to console
  echo "Checking Security Group ID: $SEC_GROUP_ID ($COUNT of $TOTAL_SEC_GROUP_IDS)"

  NETWORK_INTERFACES=`aws ec2 describe-network-interfaces --filters Name=group-id,Values=$SEC_GROUP_ID --region us-gov-west-1 --output json --profile oldcc.management | jq -r '.NetworkInterfaces[] | .NetworkInterfaceId'`

  # Check if NetworkInterfaces array is empty
  if [ -z "$NETWORK_INTERFACES" ]; then
    EMPTY_INTERFACES+=("$SEC_GROUP_ID")
  else
    NON_EMPTY_INTERFACES+=("$SEC_GROUP_ID")
  fi
done

# Output results to files
for ID in "${EMPTY_INTERFACES[@]}"; do
    echo "$ID" >> "$OUTPUT_FILE_EMPTY"
done

for ID in "${NON_EMPTY_INTERFACES[@]}"; do
    echo "$ID" >> "$OUTPUT_FILE_NON_EMPTY"
done

echo "Results have been saved to $OUTPUT_FILE_EMPTY and $OUTPUT_FILE_NON_EMPTY."
