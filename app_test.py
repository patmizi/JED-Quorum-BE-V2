import json
import os
import pytest
from app import app
from resources.test.payloads import *
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
        assert response['body'] == expected_response('expected_update_patient')

    @pytest.mark.skip(reason="Not implemented")
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

    @pytest.mark.skip(reason="Not implemented yet")
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


#
# Appointments
#
    def test_create_appointment(self, gateway_factory):
        gateway = gateway_factory()
        payload = json.dumps(create_appointment_payload)
        response = gateway.handle_request(method='POST',
                                          path='/appointments',
                                          headers=common_post_header,
                                          body=payload
                                          )
        assert response['statusCode'] == 200
        assert response['body'] == expected_response('expected_create_appointment')

    # def add_appointment(self, patient_id, doctor_id, date_start, date_end):
    #     date_start = helpers.get_datetime_from_string(date_start)
    #     date_end = helpers.get_datetime_from_string(date_end)
    #     entity = Appointment(
    #         Date_Start=date_start,
    #         Date_End=date_end,
    #         Patient_Id=patient_id,
    #         Doctor_Id=doctor_id
    #     )
    #     with DatabaseSession() as session:
    #         session.add(entity)
    #         session.flush()
    #         session.commit()
    #
    #         return self.get_appointment_by_appointment_id(appointment_id=entity.Appointment_Id)
    #
    #
    # def test_get_appointments(self, gateway_factory):
    #     gateway = gateway_factory()
    #     response = gateway.handle_request(method='GET',
    #                                       path='/appointments',
    #                                       headers={},
    #                                       body=''
    #                                       )
    #     assert response['statusCode'] == 200
    #     assert response['body'] == expected_response('expected_get_receptionist')
    # @app.route('/appointments', methods=['GET'], cors=True)
    # def get_appointments():
    #     appointment_store = AppointmentStore()
    #     appointments = appointment_store.get_all_appointments()
    #     return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)
    #
    # @app.route('/appointments/{id}', methods=['GET'], cors=True)
    # def get_appointment(id):
    #     appointment_store = AppointmentStore()
    #     appointment = appointment_store.get_appointment_by_appointment_id(id)
    #     return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)
    #
    # @app.route('/appointments/patient/{id}', methods=['GET'], cors=True)
    # def get_appointment(id):
    #     appointment_store = AppointmentStore()
    #     appointment = appointment_store.get_appointments_by_patient_id(id)
    #     return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)
    #
    # @app.route('/appointments/doctor/{id}', methods=['GET'], cors=True)
    # def get_appointment(id):
    #     appointment_store = AppointmentStore()
    #     appointment = appointment_store.get_appointments_by_doctor_id(id)
    #     return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)
    #
    # @app.route('/appointments/{id}', methods=['DELETE'], cors=True)
    # def delete_appointment(id):
    #     appointment_store = AppointmentStore()
    #     appointment_store.delete_appointment(id)
    #     return {"result": "true"}
    #
    # @app.route('/appointments/upcoming', methods=['GET'], cors=True)
    # def get_upcoming_appointments():
    #     appointment_store = AppointmentStore()
    #     appointments = appointment_store.get_all_upcoming_appointments()
    #     return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)
    #
    # @app.route('/appointments/upcoming/doctor/{id}', methods=['GET'], cors=True)
    # def get_upcoming_appointments_doctor(id):
    #     appointment_store = AppointmentStore()
    #     appointments = appointment_store.get_upcoming_appointments_by_doctor_id(id)
    #     return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)
