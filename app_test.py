import json
import os
import pytest
from app import app


@pytest.yield_fixture(autouse=True)
def set_environment():
    os.environ["DATABASE_TYPE"] = "test"
    yield
    del os.environ["DATABASE_TYPE"]


@pytest.fixture
def gateway_factory():
    from chalice.config import Config
    from chalice.local import LocalGateway

    def create_gateway(config=None):
        if config is None:
            config = Config()
        return LocalGateway(app, config)

    return create_gateway


class TestChalice(object):
    def test_hello_world(self, gateway_factory):
        print(os.environ.get('DATABASE_TYPE'))
        gateway = gateway_factory()
        response = gateway.handle_request(method='GET',
                                          path='/',
                                          headers={},
                                          body='')
        assert response['statusCode'] == 200
        assert json.loads(response['body']) == dict([('Hello', 'World')])

    def test_get_doctors(self, gateway_factory):
        print(os.environ.get('DATABASE_TYPE'))
        gateway = gateway_factory()
        response = gateway.handle_request(method='GET',
                                          path='/doctors',
                                          headers={},
                                          body=''
                                          )
        assert response['statusCode'] == 200
        assert len(json.loads(response['body'])) is not None
