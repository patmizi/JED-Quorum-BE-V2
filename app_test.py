import json
import os
import pytest
from app import app
from resources.test.payloads import register_doctor_payload, register_receptionist_payload, add_patient_payload, update_patient_payload, create_medical_case_payload, update_medical_case_payload
from resources.test.headers import common_post_header
from resources.test.expected import expected_response


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

    def test_register_doctor(self, gateway_factory):
        print(os.environ.get('DATABASE_TYPE'))
        gateway = gateway_factory()
        payload = json.dumps(register_doctor_payload)
        response = gateway.handle_request(method='POST',
                                          path='/register',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_register_doctor')

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

    def test_get_doctor(self, gateway_factory):
        print(os.environ.get('DATABASE_TYPE'))
        gateway = gateway_factory()
        response = gateway.handle_request(method='GET',
                                          path='/doctors/1',
                                          headers={},
                                          body=''
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_get_doctor')

    def test_register_receptionist(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(register_receptionist_payload)
        response = gateway.handle_request(method='POST',
                                          path='/register',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_register_receptionist')

    def test_get_receptionist(self, gateway_factory):
        gateway = gateway_factory()
        response = gateway.handle_request(method='GET',
                                          path='/receptionists/1',
                                          headers={},
                                          body=''
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_get_receptionist')

    def test_add_patient(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(add_patient_payload)
        response = gateway.handle_request(method='POST',
                                          path='/patients',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_add_patient')

    def test_update_patient(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(update_patient_payload)
        response = gateway.handle_request(method='PUT',
                                          path='/patients/1',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response()

    def test_create_medical_case(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(create_medical_case_payload)
        response = gateway.handle_request(method='POST',
                                          path='/cases',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_create_medical_case')

    def test_update_medical_case(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(create_medical_case_payload)
        response = gateway.handle_request(method='POST',
                                          path='/cases',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_update_medical_case')

