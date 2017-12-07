import requests
import random
import yaml
from pprint import pprint as print
import click

from pathgather import PathgatherClient
import pathgather.types

import feedparser

# Incase SSL validation fails, this is a horrid hack. 
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


PODCAST_URLS = [
    ('https://talkpython.fm/episodes/rss', 'talk_python_podcast')
]


@click.command()
@click.argument('server')
@click.option('--test', is_flag=True)
def load_podcasts(server, test):
    with open('.tenant.{0}.yml'.format(server), 'r') as tenant_yml:
        config = yaml.load(tenant_yml)
    client = PathgatherClient(config['pathgather_host'], config['pathgather_token'])

    for podcast, name in PODCAST_URLS:
        feed = feedparser.parse(podcast)
        for m in feed.entries:
            try:
                if not test:
                    c = client.content.create(
                        name=m['title'],
                        content_type=pathgather.types.ContentType.MEDIA,
                        source_url=m['link'],
                        provider_id=name,
                        topic_name=None,
                        level=pathgather.types.SkillLevel.ALL,
                        custom_id=None,
                        description=m['summary'],
                        image=feed['feed']['image']['href'],
                        tags=None,
                        enabled=True,
                        skills=[tag['term'] for tag in m['tags']],
                        duration=m.get('itunes_duration', 0))
                    print("Added content {0}".format(c))
            except pathgather.exceptions.PathgatherApiException as p:
                print("Failed to create content: {0}".format(p.message))

if __name__ == '__main__':
    load_podcasts()
