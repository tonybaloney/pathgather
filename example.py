from pathgather import PathgatherClient
import yaml
from pprint import pprint

with open('.tenant.yml', 'r') as tenant_yml:
    config = yaml.load(tenant_yml)

client = PathgatherClient(config['host'], config['api_key'], proxy='http://localhost:8888/', skip_ssl_validation=True)

pprint(client.users.all())

pprint(client.users.skills('362add1b-0a28-425b-a83c-40a6808fd094'))

pprint(client.paths.all())