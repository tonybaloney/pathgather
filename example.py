from pathgather import PathgatherClient
import yaml
from pprint import pprint

with open('.tenant.yml', 'r') as tenant_yml:
    config = yaml.load(tenant_yml)

client = PathgatherClient(config['host'], config['api_key'], proxy='http://localhost:8888/', skip_ssl_validation=True)
client.results_per_page = 100
# pprint(client.users.all())

# pprint(client.users.skills('362add1b-0a28-425b-a83c-40a6808fd094'))

# pprint(client.paths.all())

# pprint(client.content.log_completion(content_id='2363c93f-afa5-4663-837a-90bc47d56bf3', user_email='test@test.com'))

q = {'user': {'deactivated': {'false': '1'}},
'content': {'content_type': {'eq': 'Course'}}}

client.content.starts_and_completions(query=q)