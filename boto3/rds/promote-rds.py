import json
from datetime import datetime

import boto3


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


region = "us-east-1"

##### Initial Setup #####

rds_client = boto3.client("rds", region_name=region)

##### Promote Read Replica #####

# response = rds_client.promote_read_replica(
#     DBInstanceIdentifier='database-2'
# )

#### Describe RDS ####

response = rds_client.describe_db_instances(
    DBInstanceIdentifier="database-2",
)

# print(json.dumps(response, cls=DateTimeEncoder, ensure_ascii=False, indent=4))
db_instance = json.dumps(response, cls=DateTimeEncoder, ensure_ascii=False, indent=4)
# print(db_instance['DBInstances'])
return response["DBInstances"][0]["DBInstanceStatus"]
# print(response['DBInstances'][0]['DBInstanceStatus'])


# aws lambda invoke --function-name describe_rds --query 'DBInstanceIdentifier' output.txt
