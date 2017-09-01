#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import (BaseMockClass,
                                 mock_session_with_class,
                                 mock_session_with_fixtures)
from requests_staticmock.responses import StaticResponseFactory
import json
import pytest
from six import b
from pathgather.client import PathgatherClient
from pathgather.exceptions import PathgatherApiException


TEST_API_KEY = 'my_key_123'
TEST_TENANT = 'test.pathgather.com'
TEST_URL = 'https://{0}'.format(TEST_TENANT)


class MockClient(BaseMockClass):
    def _v1_content_4cea0449_666a_433f_8396_857e269449a9(self, request, method):
        return self.adapter.response_from_fixture(request, 'tests/fixtures/v1/users_4cea0449-666a-433f-8396-857e269449a9')


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_get_all_content():
    with mock_session_with_fixtures(client.session, 'tests/fixtures', TEST_URL):
        response = client.content.all()
        assert response[0].id == '89a07305-0122-4da1-8b40-b99f4a968f88'
        assert response[0].department.id == '90c8e4f2-3fba-4747-9322-00635bcff1bc'

