import json

from chalice import Chalice
from chalicelib.db.rel_stores import DoctorStore, ReceptionistStore, PatientStore, MedicalCaseStore
from chalicelib.lib.encoders import recursive_alchemy_encoder

app = Chalice(app_name='quorum')
app.debug = True


@app.route('/')
def index():
    return {"Hello": "World"}


##
## /cases
##
@app.route('/cases/{id}', methods=['GET'], cors=True)
def get_medical_case(id):
    medical_case_store = MedicalCaseStore()
    case = medical_case_store.get_medical_case(id)
    print(case)
    return json.dumps(case, cls=recursive_alchemy_encoder(), check_circular=False)


# @app.route('/cases', methods=['POST'], cors=True)
# def create_medical_case():
#     medical_case_store = MedicalCaseStore()
#     body_json = app.current_request.json_body
#     print(body_json)
#     return { "Value": True }

##
## /patients
##
@app.route('/patients', methods=['GET'], cors=True)
def get_patients():
    patient_store = PatientStore()
    patients = patient_store.get_all_patients()
    print(patients)
    return json.dumps(patients, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/patients/{id}', methods=['GET'], cors=True)
def get_patient(id):
    patient_store = PatientStore()
    patient = patient_store.get_patient(id)
    print(patient)
    return json.dumps(patient, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/patients', methods=['POST'], cors=True)
def add_patient():
    post_body = app.current_request.json_body
    patient_store = PatientStore()
    data = {}
    if 'address' in post_body:
        data['address'] = post_body['address']

    patient = patient_store.add_patient(
        first_name=post_body.get('First_Name'),
        last_name=post_body.get('Last_Name'),
        gender=post_body.get('Gender'),
        date_of_birth=post_body.get('Date_Of_Birth'),
        contact_number=post_body.get('Contact_Number'),
        email=post_body.get('Email'),
        data=data
    )

    print(patient)
    return json.dumps(patient, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/patients/{id}', methods=['DELETE'], cors=True)
def delete_patient(id):
    patient_store = PatientStore()
    patient_store.delete_patient(patient_id=id)
    return {"result": "true"}


##
## /doctors
##
@app.route('/doctors/{id}', methods=['GET'], cors=True)
def get_doctor(id):
    doctor_store = DoctorStore()
    doctor = doctor_store.get_doctor(id)
    print(doctor)
    return json.dumps(doctor, cls=recursive_alchemy_encoder(), check_circular=False)


# @app.route('/doctors/{id}', methods=['PATCH'], cors=True)
# def update_doctor(id):
#     doctor_store = DoctorStore()
#     updated_doctor = doctor_store.update_doctor(id)
#     print(updated_doctor)
#     return json.dumps(updated_doctor, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/doctors', methods=['GET'], cors=True)
def get_doctors():
    print("[*] Get all doctors...")
    doctor_store = DoctorStore()
    doctors = doctor_store.get_all_doctors()
    return json.dumps(doctors, cls=recursive_alchemy_encoder(), check_circular=False)


##
## /receptionists
##
@app.route('/receptionists/{id}', methods=['GET'], cors=True)
def get_receptionist(id):
    receptionist_store = ReceptionistStore()
    receptionist = receptionist_store.get_receptionist(id)
    print(receptionist)
    return json.dumps(receptionist, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/receptionists/{id}', methods=['PATCH'], cors=True)
def update_receptionist(id):
    receptionist_store = ReceptionistStore()
    updated_receptionist = receptionist_store.update_receptionist(id)
    print(update_receptionist)
    return json.dumps(updated_receptionist, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/receptionists', methods=['GET'], cors=True)
def get_receptionists():
    print("[*] Get all receptionists...")
    receptionist_store = ReceptionistStore()
    receptionists = receptionist_store.get_all_receptionists()
    return json.dumps(receptionists, cls=recursive_alchemy_encoder(), check_circular=False)


#
# Registration hook
#
@app.route('/register', methods=['POST'], cors=True)
def register_user():
    print("[*] Registering new user...")
    user_json = app.current_request.json_body
    user_metadata = user_json['user']['user_metadata']
    data = {"User_Id": user_json['user']['id']}
    if 'address' in user_metadata:
        data['address'] = user_metadata.get('address')

    if user_metadata['business_role'] == 'doctor':
        app.log.info('Registering a doctor...')
        doctor_store = DoctorStore()
        doctor_store.create_doctor(
            first_name=user_metadata.get('first_name', 'User'),
            last_name=user_metadata.get('last_name', ''),
            gender=user_metadata.get('gender', 'M'),
            date_of_birth=user_metadata.get('date_of_birth', ''),
            contact_number=user_metadata.get('contact_number', ''),
            email=user_metadata.get('email', ''),
            data=data
        )
    elif user_metadata['business_role'] == 'receptionist':
        app.log.info('Registering a receptionist')
        receptionist_store = ReceptionistStore()
        receptionist_store.create_receptionist(
            first_name=user_metadata.get('first_name', 'User'),
            last_name=user_metadata.get('last_name', ''),
            gender=user_metadata.get('gender', 'M'),
            date_of_birth=user_metadata.get('date_of_birth', ''),
            contact_number=user_metadata.get('contact_number', ''),
            email=user_metadata.get('email', ''),
            data=data
        )
    else:
        app.log.error('[x] BUSINESS ROLE NOT FOUND')
        raise ValueError('business_role')
    return {"result": "true"}
