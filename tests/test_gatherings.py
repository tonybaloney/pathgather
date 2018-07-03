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
from pathgather.client import PathgatherClient


TEST_API_KEY = "my_key_123"
TEST_TENANT = "test.pathgather.com"
TEST_URL = "https://{0}".format(TEST_TENANT)

client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


class MockClient(BaseMockClass):
    def _v1_gatherings(self, request, method):
        assert method == "POST"
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/gatherings_3578d16a-381a-4041-a6bb-1b3957fc8e94"
        )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/gatherings_3578d16a-381a-4041-a6bb-1b3957fc8e94"
        )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_users(
        self, request, method
    ):
        if method == "GET":
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/gatherings_users"
            )
        else:
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/gatherings_users_single"
            )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_gathering_invites(
        self, request, method
    ):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/gatherings_invite"
        )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_contents(
        self, request, method
    ):
        if method == "GET":
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/gatherings_contents"
            )
        else:
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/gatherings_contents_single"
            )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_users_9dbd1b62_2d6e_414a_9e4c_253d17693f09(
        self, request, method
    ):
        assert method == "DELETE"
        return StaticResponseFactory.GoodResponse(b"", request)

    def _v1_recommendation_to_gathering(self, request, method):
        return self.adapter.response_from_fixture(
            request, "tests/fixtures/v1/gatherings_recommendation"
        )

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_contents_9dbd1b62_2d6e_414a_9e4c_253d17693f09(
        self, request, method
    ):
        assert method == "DELETE"
        return StaticResponseFactory.GoodResponse(b"", request)

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_paths_9dbd1b62_2d6e_414a_9e4c_253d17693f09(
        self, request, method
    ):
        assert method == "DELETE"
        return StaticResponseFactory.GoodResponse(b"", request)

    def _v1_gatherings_3578d16a_381a_4041_a6bb_1b3957fc8e94_paths(
        self, request, method
    ):
        if method == "GET":
            return self.adapter.response_from_fixture(
                request, "tests/fixtures/v1/gatherings_paths"
            )


def test_get_all_gatherings():
    with mock_session_with_fixtures(client.session, "tests/fixtures", TEST_URL):
        response = client.gatherings.all()
        assert response[0].id == "3578d16a-381a-4041-a6bb-1b3957fc8e94"
        assert response[0].name == "Learn to Code"
        assert response[0].user.first_name == "Anthony"


def test_get_gathering():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.get("3578d16a-381a-4041-a6bb-1b3957fc8e94")
        assert response.id == "3578d16a-381a-4041-a6bb-1b3957fc8e94"
        assert response.name == "Learn to Code"
        assert response.user.first_name == "Anthony"
        assert response.skills[0].name == "Python"


def test_create_gathering():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.create("Learn to Code")
        assert response.id == "3578d16a-381a-4041-a6bb-1b3957fc8e94"
        assert response.name == "Learn to Code"
        assert response.user.first_name == "Anthony"
        assert response.skills[0].name == "Python"


def test_update_gathering():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.update(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94", name="Learn to Code"
        )
        assert response.id == "3578d16a-381a-4041-a6bb-1b3957fc8e94"
        assert response.name == "Learn to Code"
        assert response.user.first_name == "Anthony"
        assert response.skills[0].name == "Python"


def test_delete_gathering():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.delete("3578d16a-381a-4041-a6bb-1b3957fc8e94")
        assert response is None


def test_get_gathering_users():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.users("3578d16a-381a-4041-a6bb-1b3957fc8e94")
        assert response[0].gathering.id == "3578d16a-381a-4041-a6bb-1b3957fc8e94"
        assert response[0].gathering.name == "Learn to Code"
        assert response[0].user.first_name == "Anthony"


def test_add_gathering_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.invite_user(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94",
            "9dbd1b62-2d6e-414a-9e4c-253d17693f09",
        )
        assert response.inviter.first_name == "Anthony"
        assert response.invitee.first_name == "Lee"


def test_delete_gathering_user():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.remove_user(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94",
            "9dbd1b62-2d6e-414a-9e4c-253d17693f09",
        )
        assert response is None


def test_get_gathering_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.content("3578d16a-381a-4041-a6bb-1b3957fc8e94")
        assert response[0].user.first_name == "Anthony"
        assert response[0].course.name == "The Hour of Code is here"
        assert response[0].course.reviews_count == 0
        assert response[0].course.sharer.first_name == "Anthony"


def test_add_gathering_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.add_content(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94",
            "9dbd1b62-2d6e-414a-9e4c-253d17693f09",
        )
        assert response["gathering_recommendations_count"] == 1


def test_delete_gathering_content():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.remove_content(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94",
            "9dbd1b62-2d6e-414a-9e4c-253d17693f09",
        )
        assert response is None


def test_get_gathering_paths():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.paths("3578d16a-381a-4041-a6bb-1b3957fc8e94")
        assert response[0].user.first_name == "Anthony"
        assert response[0].path.name == "Pathgather for L&D Managers"
        assert response[0].path.user_started_count == 16


def test_delete_gathering_path():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.gatherings.remove_path(
            "3578d16a-381a-4041-a6bb-1b3957fc8e94",
            "9dbd1b62-2d6e-414a-9e4c-253d17693f09",
        )
        assert response is None
