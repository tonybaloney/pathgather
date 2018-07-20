#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import (
    BaseMockClass,
    mock_session_with_class,
    mock_session_with_fixtures,
)
from requests_staticmock.responses import StaticResponseFactory
from six import b
from pathgather.client import PathgatherClient
from pathgather.types_ import SkillLevel
from pathgather.models.skill import Skill, UserSkill


TEST_API_KEY = "my_key_123"
TEST_TENANT = "test.pathgather.com"
TEST_URL = "https://{0}".format(TEST_TENANT)
TEST_ID = "c57f2bc8-d69d-42ba-bbcb-2a62c1a14f6f"
TEST_SKILL = Skill(id="12345", name="Ruby")
TEST_USER_SKILL_ID = "f5bf30a8-412c-4cea-9a64-1d4aae5a40f9"


class MockClient(BaseMockClass):
    def _v1_providers_c57f2bc8_d69d_42ba_bbcb_2a62c1a14f6f(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/providers_single"
        )

    def _v1_providers(self, request, method):
        if method in ["POST", "PUT"]:
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/providers_single"
            )
        elif method == "DELETE":
            return StaticResponseFactory.GoodResponse(
                request=request, body=b(""), status_code=200
            )


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_all_providers():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.providers.all()
        assert response[5].id == "fd0bcc42-05ff-443e-9c13-523025bad80a"
        assert response[5].name == "Talk Python to Me Podcast"
        assert response[5].custom_id == "talk_python_podcast"
        assert response[5].created_at.timestamp == 1512682775
        assert response[5].created_at == response[5].updated_at
        assert not response[5].may_require_vpn
        assert not response[5].may_not_be_mobile_friendly
        assert response[5].is_subscribed


def test_get_providers():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.providers.get(TEST_ID)
        assert response.id == TEST_ID


def test_create_provider():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.providers.create("Bobby no mates", "custom-skill")
        assert response.id == TEST_ID


def test_delete_provider():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.providers.delete(TEST_ID)
        assert response is None
