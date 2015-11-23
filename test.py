import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
files = response.read()
first, second= files.split(':', 2)
print first
print second
