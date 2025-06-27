my_route_tables=vpc_1.route_tables.all()

route_tables=ec2client.describe_route_tables(Filters=[{"Name":"vpc-id","Values":[vpc_1.id]}])

