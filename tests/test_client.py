#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import BaseMockClass, mock_session_with_class
from requests_staticmock.responses import StaticResponseFactory
import json
import pytest
from six import b
from pathgather.client import PathgatherClient
from pathgather.exceptions import PathgatherApiException


TEST_API_KEY = "my_key_123"
TEST_TENANT = "test.pathgather.com"
TEST_URL = "https://{0}".format(TEST_TENANT)


class MockClient(BaseMockClass):
    def _v1_headers(self, request, headers):
        if (
            "Authorization" not in headers.keys()
            or TEST_API_KEY not in headers["Authorization"]
        ):
            return json.dumps({"good": False})
        else:
            return json.dumps({"good": True})

    def _v1_get(self, method):
        return json.dumps({"good": method == "GET"})

    def _v1_get_bad(self, request, method):
        if method == "GET":
            return StaticResponseFactory.BadResponse(
                request=request, body=b("bad request"), status_code=500
            )

    def _v1_post(self, method):
        return json.dumps({"good": method == "POST"})

    def _v1_post_bad(self, request, method):
        if method == "POST":
            return StaticResponseFactory.BadResponse(
                request=request, body=b("bad request"), status_code=500
            )

    def _v1_put(self, method):
        return json.dumps({"good": method == "PUT"})

    def _v1_put_bad(self, request, method):
        if method == "PUT":
            return StaticResponseFactory.BadResponse(
                request=request, body=b("bad request"), status_code=500
            )

    def _v1_delete(self, method):
        return json.dumps({"good": method == "DELETE"})

    def _v1_delete_bad(self, request, method):
        if method == "DELETE":
            return StaticResponseFactory.BadResponse(
                request=request, body=b("bad request"), status_code=500
            )


client = PathgatherClient(TEST_TENANT, TEST_API_KEY)


def test_base_url():
    assert TEST_TENANT in client.base_url


def test_headers():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.get("headers")
        assert response["good"]


def test_get_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.get("get")
        assert response["good"]


def test_get_bad_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        with pytest.raises(PathgatherApiException):
            client.get("get/bad")


def test_post_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.post("post")
        assert response["good"]


def test_post_bad_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        with pytest.raises(PathgatherApiException):
            client.post("post/bad")


def test_put_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        response = client.put("put")
        assert response is not None


def test_put_bad_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        with pytest.raises(PathgatherApiException):
            client.put("put/bad")


def test_delete_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        client.delete("delete")
        assert True


def test_delete_bad_request():
    with mock_session_with_class(client.session, MockClient, TEST_URL):
        with pytest.raises(PathgatherApiException):
            client.delete("delete/bad")
