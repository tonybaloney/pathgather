#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import (BaseMockClass,
                                 mock_session_with_class,
                                 mock_session_with_fixtures)
from requests_staticmock.responses import StaticResponseFactory
from six import b
from pathgather.client import PathgatherClient
from pathgather.types_ import SkillLevel
from pathgather.models.skill import Skill, UserSkill


TEST_API_KEY = 'my_key_123'
TEST_TENANT = 'test.pathgather.com'
TEST_URL = 'https://{0}'.format(TEST_TENANT)
TEST_PATH_ID = '57a89e01-59a9-4c39-8b64-4eabd512e9f5'


class MockClient(BaseMockClass):
    def _v1_paths_57a89e01_59a9_4c39_8b64_4eabd512e9f5(self, request, method):
        return self.adapter.response_from_fixture(request, 'tests/fixtures/v1/path_57a89e01-59a9-4c39-8b64-4eabd512e9f5')

client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_all_paths():
    with mock_session_with_fixtures(client.session, 'tests/fixtures', TEST_URL):
        response = client.paths.all()
        assert response[0].id == TEST_PATH_ID
        assert response[0].user.first_name == 'Anthony'
        assert response[0].skills[0].name == 'Learning and Development'


def test_get_path():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.paths.get(TEST_PATH_ID)
        assert response.id == TEST_PATH_ID


def test_get_path_completions():
    with mock_session_with_fixtures(client.session, 'tests/fixtures', TEST_URL):
        response = client.paths.starts_and_completions()
        assert response[0].id == 'e3904e76-2405-4a69-8e6e-40f9ac4674c7'
        assert response[0].path.user.first_name == 'Test'
        assert response[0].user.last_name == u'Morley ⓨ'
        assert response[0].path.name == 'Pathgather for L&D Managers'
