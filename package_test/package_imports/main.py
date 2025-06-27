# Importing models package
import common
from common import models, validators

validators.is_json("{}")
validators.is_date("2018-01-01")
validators.is_boolean(True)

print("\n\n***** self *****")
for k in dict(globals()).keys():
    print(k)

print("\n\n***** common *****")
for k in common.__dict__.keys():
    print(k)

print("\n\n***** validators *****")
for k in validators.__dict__.keys():
    print(k)




print("\n\n***** models *****")
for k in models.__dict__.keys():
    print(k)


john_post = models.Post()
john_posts = models.Posts()
john = models.Users()
