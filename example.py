from pathgather import PathgatherClient
import yaml
import json
from pprint import pprint

with open('.tenant.yml', 'r') as tenant_yml:
    config = yaml.load(tenant_yml)

client = PathgatherClient(config['host'], config['api_key'])

pprint(client.users.all())
