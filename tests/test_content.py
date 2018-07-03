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
from pathgather.client import PathgatherClient
from pathgather.types_ import ContentType, SkillLevel


TEST_API_KEY = "my_key_123"
TEST_TENANT = "test.pathgather.com"
TEST_URL = "https://{0}".format(TEST_TENANT)
TEST_CONTENT_ID = "89a07305-0122-4da1-8b40-b99f4a968f88"
TEST_USER_ID = "9dbd1b62-2d6e-414a-9e4c-253d17693f09"


class MockClient(BaseMockClass):
    def _v1_content(self, request, method):
        assert method == "POST"
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88"
        )

    def _v1_content_89a07305_0122_4da1_8b40_b99f4a968f88(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88"
        )

    def _v1_user_content(self, request, method):
        assert method == "POST"
        return self.adapter.response_from_fixture(
            request,
            "tests/fixtures/v1/user_content_650a4eb1-eff8-4032-aef0-ee5a66ab61b1",
        )

    def _v1_content_89a07305_0122_4da1_8b40_b99f4a968f88_comments(
        self, request, method
    ):
        if method == "GET":
            return self.adapter.response_from_fixture(
                request,
                "tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88_comments",
            )
        elif method == "POST":
            return self.adapter.response_from_fixture(
                request,
                "tests/fixtures/v1/content_89a07305-0122-4da1-8b40-b99f4a968f88_comments_create",
            )


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_get_all_content():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.content.all()
        assert response[0].id == TEST_CONTENT_ID
        assert response[0].name == "ADO.NET Fundamentals"


def test_get_all_content_query():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.content.all(query={"a": 1})
        assert response[0].id == TEST_CONTENT_ID
        assert response[0].name == "ADO.NET Fundamentals"


def test_get_all_content_filter():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.content.all(filter="shared")
        assert response[0].id == TEST_CONTENT_ID
        assert response[0].name == "ADO.NET Fundamentals"


def test_get_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.get(TEST_CONTENT_ID)
        assert response.id == TEST_CONTENT_ID
        assert response.name == "Networking Basics"
        assert response.provider.name == "Cisco Learning Labs"


def test_create_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.create(
            "test",
            ContentType.WEBPAGE,
            "url://test.com/page",
            "Pluralsight",
            "topic",
            SkillLevel.ADVANCED,
            custom_id=None,
            description=None,
            image=None,
            tags=None,
            enabled=True,
            skills=None,
            duration=None,
        )
        assert response.id == TEST_CONTENT_ID
        assert response.name == "Networking Basics"
        assert response.provider.name == "Cisco Learning Labs"


def test_update_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.update(TEST_CONTENT_ID, description="new description")
        assert response.id == TEST_CONTENT_ID
        assert response.name == "Networking Basics"
        assert response.provider.name == "Cisco Learning Labs"


def test_user_content():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.content.starts_and_completions()
        assert response[0].id == "f41f88d2-c9f0-4f5d-9dcc-c3c6c33d7e6d"
        assert response[0].content.name == "PathGather first 5 minutes"
        assert response[0].content.provider.name == "youtu.be"
        assert response[0].user.first_name == "non"


def test_log_completion():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.log_completion(
            content_id="650a4eb1-eff8-4032-aef0-ee5a66ab61b1",
            user_email="test@test.com",
        )
        assert response.id == "650a4eb1-eff8-4032-aef0-ee5a66ab61b1"
        assert (
            response.content.name
            == "How to open and close presentations? - Presentation lesson from Mark Powell"
        )
        assert response.content.provider.name == "youtube.com"
        assert response.user.first_name == "Anthony"


def test_get_content_comments():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.get_comments(TEST_CONTENT_ID)
        assert len(response) == 1
        assert response[0].message == "hello from bot"
        assert response[0].user.first_name == "DDU"


def test_create_content_comment():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.content.create_comment(
            TEST_CONTENT_ID, "hello from bot", TEST_USER_ID
        )
        assert response.message == "hello from bot"
        assert response.user.first_name == "DDU"
        assert (
            response.content.name
            == "No serial number - how we log it in ITSM / BranchTrack"
        )
