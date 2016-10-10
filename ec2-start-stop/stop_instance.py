import boto3
from boto3.session import Session

running_instances_list = []
session = Session(aws_access_key_id='xxxxx',aws_secret_access_key='xxxxxxx',region_name='us-east-1')

ec2=session.resource('ec2')

filters= [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

instances = ec2.instances.filter(Filters=filters)

for instance in instances:
	running_instances_list.append(instance.id)


ec2.instances.filter(InstanceIds=running_instances_list).stop()
print "Stopped instances:",running_instances_list

