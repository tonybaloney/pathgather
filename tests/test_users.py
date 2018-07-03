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
    def _v1_users_4cea0449_666a_433f_8396_857e269449a9(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/users_4cea0449-666a-433f-8396-857e269449a9"
        )

    def _v1_users_4cea0449_666a_433f_8396_857e269449a9_user_skills(
        self, request, method
    ):
        if method == "GET":
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/users_skills"
            )
        if method == "POST":
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/users_skill"
            )

    def _v1_users_4cea0449_666a_433f_8396_857e269449a9_user_skills_f5bf30a8_412c_4cea_9a64_1d4aae5a40f9(
        self, request, method
    ):
        if method == "DELETE":
            return StaticResponseFactory.GoodResponse(
                request=request, body=b(""), status_code=200
            )

    def _v1_users(self, request, method):
        if method in ["POST", "PUT"]:
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/users_4cea0449-666a-433f-8396-857e269449a9"
            )
        elif method == "DELETE":
            return StaticResponseFactory.GoodResponse(
                request=request, body=b(""), status_code=200
            )


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_all_users():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.users.all()
        assert response[0].id == TEST_USER_ID
        assert response[0].department.id == "90c8e4f2-3fba-4747-9322-00635bcff1bc"


def test_get_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.get(TEST_USER_ID)
        assert response.id == TEST_USER_ID


def test_create_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.create(
            "Bobby no mates",
            "lord of all",
            "boss place",
            "lord@place.com",
            saml_id=None,
            custom_id=None,
            hire_date=None,
            location="",
            avatar="",
            admin=False,
            send_invite=True,
            deactivated=False,
            custom_fields=None,
        )
        assert response.id == TEST_USER_ID


def test_update_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.update(
            TEST_USER_ID,
            "Bobby no mates",
            "lord of all",
            "boss place",
            "lord@place.com",
            saml_id=None,
            custom_id=None,
            hire_date=None,
            location="",
            avatar="",
            admin=False,
            deactivated=False,
            custom_fields=None,
        )
        assert response.id == TEST_USER_ID


def test_delete_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.delete(TEST_USER_ID)


def test_get_user_skills():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.skills(TEST_USER_ID)
        assert len(response) == 3
        assert response[1].level == SkillLevel.INTERMEDIATE
        assert response[1].skill.name == "Ruby"


def test_add_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.add_skill(TEST_USER_ID, TEST_SKILL, SkillLevel.ALL)
        assert response.level == SkillLevel.EXPERT


def test_add_skill_by_id():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.add_skill_by_id(
            TEST_USER_ID, TEST_SKILL.id, SkillLevel.ALL
        )
        assert response.level == SkillLevel.EXPERT


def test_add_skill_by_name():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.add_skill_by_name(
            TEST_USER_ID, TEST_SKILL.name, SkillLevel.ALL
        )
        assert response.level == SkillLevel.EXPERT


def test_update_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.update_skill_level(
            TEST_USER_ID, TEST_SKILL, SkillLevel.INTERMEDIATE
        )
        assert response.level == SkillLevel.EXPERT


def test_delete_skill():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.users.delete_skill(
            TEST_USER_ID, "f5bf30a8-412c-4cea-9a64-1d4aae5a40f9"
        )
        assert response is None

        response = client.users.delete_skill(
            TEST_USER_ID,
            UserSkill(
                id=TEST_USER_SKILL_ID, level=SkillLevel.BEGINNER, skill=TEST_SKILL
            ),
        )
        assert response is None
