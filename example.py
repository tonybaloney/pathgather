from pathgather import PathgatherClient
import yaml

with open('.tenant.yml', 'r') as tenant_yml:
    config = yaml.load(tenant_yml)

client = PathgatherClient(config['host'], config['api_key'])

print(client.users.get_all_users())