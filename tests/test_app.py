from cgitb import reset
from urllib import response
from wsgiref import headers

import pytest
from src.app import *


@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "DEBUG": True})
    yield app


@pytest.fixture()
def client(app):
    yield app.test_client()


@pytest.fixture()
def runner(app):
    yield app.test_cli_runner()


def test_ip(client):
    response = client.get("/ip")
    assert response.status_code == 200
    assert response.data == b"127.0.0.1"


def test_forwarder(client):
    response = client.get("/ip", headers={"X-Forwarded-For": "8.8.8.8"})
    assert response.status_code == 200
    assert response.data == b"8.8.8.8"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Nothing here"


def test_memcached(client):
    response = client.get("/memcached")
    assert response.status_code == 200
    assert response.data == b"False"
