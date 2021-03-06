#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
files = response.read()
first, second= files.split(':', 2)
# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = first
secret_access_key = second

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
first_arg = sys.argv[1]
second_arg = sys.argv[2]

# Get a list of the queues that exists and then print the list out
conn.send_message(first_arg, second_arg)
