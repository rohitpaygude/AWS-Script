import boto3
from boto3.session import Session

stopped_instances_list = []
session = Session(aws_access_key_id='xxxxxxx',aws_secret_access_key='xxxxxxxxxx',region_name='us-east-1')

ec2=session.resource('ec2')
filters= [{
            'Name': 'tag:AutoOn',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
instances = ec2.instances.filter(Filters=filters)

for instance in instances:
	stopped_instances_list.append(instance.id)

ec2.instances.filter(InstanceIds=stopped_instances_list).start()

print "instance starting:",stopped_instances_list

