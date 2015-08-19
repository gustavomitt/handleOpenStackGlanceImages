'''
Created on 18 de ago de 2015

@author: Gustavo Mitt
'''

from keystoneclient.auth.identity import v2 as identity
from keystoneclient import session
from glanceclient import Client
import os
import re

auth = identity.Password(auth_url=os.environ['OS_AUTH_URL'],
                         username=os.environ['OS_USERNAME'],
                         password=os.environ['OS_PASSWORD'],
                         tenant_name=os.environ['OS_TENANT_NAME'])

sess = session.Session(auth=auth)
token = auth.get_token(sess)

glance = Client('2',
                endpoint=os.environ['OS_GLANCE_ENDPOINT'],
                token=token)

for image in glance.images.list():
    # Snapshots are in raw format. Use this way to remove snapshots from backup
    # Needs a elegant way to do that
    if image.disk_format == "raw":
        pass
    else:
        # Remove "(" and ")" from filename
        # TODO: add all not allowed characters
        name = re.sub('[/(/)]','_',image.name)
        filename = name + "." + image.disk_format
        image_file = open(filename, 'w+')
        for chunk in glance.images.data(image.id):
            image_file.write(chunk)
        print "Image wrote: " + filename
    
    
   
