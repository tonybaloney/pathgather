from pathgather import PathgatherClient
import yaml
import json
from pprint import pprint

with open('.tenant.yml', 'r') as tenant_yml:
    config = yaml.load(tenant_yml)

client = PathgatherClient(config['host'], config['api_key'], 'https://localhost:8888/', True)

pprint(client.users.all())


#with open('dump.json', 'r') as dump_j:
#    data = json.load(dump_j)

#for user in data['users']:
#    print('Creating {0}'.format(user['full_name']))
#    new_user = client.users.create(
#        name=user['full_name'], 
#        job_title=user['job_title'],
#        department='Learning and Development',
#        email=user['email'])
#    print(new_user)
