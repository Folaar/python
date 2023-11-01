import boto3
from pprint import pprint
s3_instance =boto3.client('s3')
i_am_instance= boto3.client('iam')

users= i_am_instance.list_users()
pprint(users)