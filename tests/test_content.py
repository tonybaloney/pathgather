#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import (BaseMockClass,
                                 mock_session_with_class,
                                 mock_session_with_fixtures)
from pathgather.client import PathgatherClient
from pathgather.types import ContentType, SkillLevel


TEST_API_KEY = 'my_key_123'
TEST_TENANT = 'test.pathgather.com'
TEST_URL = 'https://{0}'.format(TEST_TENANT)


class MockClient(BaseMockClass):
    def _v1_content(self, request, method):
        assert method == 'POST'
        return self.adapter.response_from_fixture(request, 'tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88')

    def _v1_content_89a07305_0122_4da1_8b40_b99f4a968f88(self, request, method):
        return self.adapter.response_from_fixture(request, 'tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88')


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_get_all_content():
    with mock_session_with_fixtures(client.session, 'tests/fixtures', TEST_URL):
        response = client.content.all()
        assert response[0].id == '89a07305-0122-4da1-8b40-b99f4a968f88'
        assert response[0].name == "ADO.NET Fundamentals"

def test_get_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.get('89a07305-0122-4da1-8b40-b99f4a968f88')
        assert response.id == '89a07305-0122-4da1-8b40-b99f4a968f88'
        assert response.name == "ADO.NET Fundamentals"
        assert response.provider.name == 'Pluralsight'

def test_create_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.create(
            'test',
            ContentType.WEBPAGE,
            'url://test.com/page',
            'Pluralsight', 
            'topic',
            SkillLevel.ADVANCED, custom_id=None,
            description=None, image=None, tags=None, enabled=True,
            skills=None, duration=None)
        assert response.id == '89a07305-0122-4da1-8b40-b99f4a968f88'
        assert response.name == "ADO.NET Fundamentals"
        assert response.provider.name == 'Pluralsight'
