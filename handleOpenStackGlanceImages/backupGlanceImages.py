'''
Created on 18 de ago de 2015

@author: Owner
'''

from keystoneclient.auth.identity import v2 as identity
from keystoneclient import session
from glanceclient import Client

auth = identity.Password(auth_url="http://10.151.13.4:35357/v2.0",
                         username="admin",
                         password="Laboratorio",
                         tenant_name="admin")

sess = session.Session(auth=auth)
token = auth.get_token(sess)

glance = Client('2',
                endpoint="http://10.151.13.2:9292",
                token=token)

for image in glance.images.list():
   print image
