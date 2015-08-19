'''
Created on 18 de ago de 2015

@author: Gustavo Mitt
'''

from keystoneclient.auth.identity import v2 as identity
from keystoneclient import session
from glanceclient import Client

auth = identity.Password(auth_url=OS_AUTH_URL,
                         username=OS_USERNAME,
                         password=OS_PASSWORD,
                         tenant_name=OS_TENANT_NAME)

sess = session.Session(auth=auth)
token = auth.get_token(sess)

glance = Client('2',
                endpoint=OS_GLANCE_ENDPOINT,
                token=token)

for image in glance.images.list():
    print image
   
cirros = glance.images.get("fd2c1699-fe0b-4c8d-8a4b-065831fe6360")

d = glance.images.data(cirros.id)

filename = cirros.name + "." + cirros.disk_format

image_file = open(filename, 'w+')

for chunk in glance.images.data(cirros.id):
    image_file.write(chunk)
