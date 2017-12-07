import requests
import random
import yaml
from pprint import pprint as print
import click

from pathgather import PathgatherClient
import pathgather.types


@click.command()
@click.argument('server')
@click.option('--test', is_flag=True)
def scrape_cisco_learning(server, test):
    r = random.random()*1000000
    with open('.tenant.{0}.yml'.format(server), 'r') as tenant_yml:
        config = yaml.load(tenant_yml)

    CONTENT_URL = 'https://learninglabs.cisco.com/api/labModules/public?cacheBuster={0}&_pageSize=100&_search=true&_sortBy=seq+asc'.format(int(r))
    BASE_URL = 'https://learninglabs.cisco.com/modules/'
    modules = []
    with requests.Session() as session:
        req = session.get(CONTENT_URL)

        response = req.json()

        modules = response['items']

    client = PathgatherClient(
        config['pathgather_host'], config['pathgather_token'])

    for m in modules:
        try:
            if not test:
                c = client.content.create(
                    name=m['title'],
                    content_type=pathgather.types.ContentType.COURSE,
                    source_url=BASE_URL + m['permalink'],
                    provider_id='cisco_learning_labs',
                    topic_name='Cisco',
                    level=pathgather.types.SkillLevel.ALL,
                    custom_id=None,
                    description=m['desc'],
                    image=None,
                    tags=None,
                    enabled=True,
                    skills=['Cisco'],
                    duration='{0} min'.format(m.get('time', 0)))
            print("Added content {0}".format(c))
        except pathgather.exceptions.PathgatherApiException as p:
            print("Failed to create content: {0}".format(p.message))

if __name__ == '__main__':
    scrape_cisco_learning()
