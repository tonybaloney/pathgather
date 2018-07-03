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
TEST_USER_ID = "4cea0449-666a-433f-8396-857e269449a9"
TEST_SKILL = Skill(id="12345", name="Ruby")
TEST_USER_SKILL_ID = "f5bf30a8-412c-4cea-9a64-1d4aae5a40f9"


class MockClient(BaseMockClass):
    def _v1_skills_4cea0449_666a_433f_8396_857e269449a9(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/skills_single"
        )

    def _v1_skills(self, request, method):
        if method in ["POST", "PUT"]:
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/skills_single"
            )
        elif method == "DELETE":
            return StaticResponseFactory.GoodResponse(
                request=request, body=b(""), status_code=200
            )


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_all_skills():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.skills.all()
        assert response[0].id == "5b122717-6b68-4614-889c-be1b15391891"
        assert response[0].name == "data science"


def test_get_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.skills.get(TEST_USER_ID)
        assert response.id == "5b122717-6b68-4614-889c-be1b15391891"


def test_create_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.skills.create("Bobby no mates", "custom-skill")
        assert response.id == "5b122717-6b68-4614-889c-be1b15391891"


def test_update_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.skills.update(TEST_USER_ID, "Bobby no mates", "lord of all")
        assert response.id == "5b122717-6b68-4614-889c-be1b15391891"


def test_delete_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.skills.delete(TEST_USER_ID)
        assert response is None
