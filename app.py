import json

from chalice import Chalice
from chalicelib.db.rel_stores import DoctorStore, ReceptionistStore, PatientStore, MedicalCaseStore, AppointmentStore
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
    print("Case id = " + id)
    medical_case_store = MedicalCaseStore()
    case = medical_case_store.get_medical_case(id)
    return json.dumps(case, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/cases', methods=['POST'], cors=True)
def case_patient():
    post_body = app.current_request.json_body
    medical_case_store = MedicalCaseStore()
    data = {}
    if post_body.get('doctors') is not None:
        data['doctors'] = post_body.get('doctors')
    case = medical_case_store.add_medical_case(
        medical_case_name=post_body.get('Medical_Case_Name'),
        medical_case_description=post_body.get('Medical_Case_Description'),
        patient_id=post_body.get('Patient_Id'),
        data=data
    )
    print(case)
    return json.dumps(case, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/cases/{id}', methods=['PUT'], cors=True)
def update_medical_case(id):
    post_body = app.current_request.json_body
    medical_case_store = MedicalCaseStore()
    data = {}
    if post_body.get('doctors') is not None:
        data['doctors'] = post_body.get('doctors')
    case = medical_case_store.update_medical_case(
        medical_case_id=id,
        medical_case_name=post_body.get('Medical_Case_Name'),
        medical_case_description=post_body.get('Medical_Case_Description'),
        patient_id=post_body.get('Patient_Id'),
        data=data
    )
    print(case)
    return json.dumps(case, cls=recursive_alchemy_encoder(), check_circular=False)


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

@app.route('/patients/{id}', methods=['PUT'], cors=True)
def update_patient(id):
    post_body = app.current_request.json_body
    patient_store = PatientStore()
    if post_body.get('cases') is not None:
        post_body.pop('cases', None)
    patient = patient_store.update_patient(patient_id=id, params=post_body)
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


# @app.route('/doctors/{id}', methods=['PUT'], cors=True)
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
    print(user_json)
    user_metadata = user_json['user']['user_metadata']
    data = {"User_Id": user_json['user']['id']}
    if 'address' in user_metadata:
        data['address'] = user_metadata.get('address')

    if user_metadata['Business_Role'] == 'doctor':
        app.log.info('Registering a doctor...')
        doctor_store = DoctorStore()
        doctor_store.create_doctor(
            first_name=user_metadata.get('First_Name', 'User'),
            last_name=user_metadata.get('Last_Name', ''),
            gender=user_metadata.get('Gender', 'M'),
            date_of_birth=user_metadata.get('Date_Of_Birth', ''),
            contact_number=user_metadata.get('Contact_Number', ''),
            email=user_metadata.get('Email', ''),
            data=data
        )
    elif user_metadata['Business_Role'] == 'receptionist':
        app.log.info('Registering a receptionist')
        receptionist_store = ReceptionistStore()
        receptionist_store.create_receptionist(
            first_name=user_metadata.get('First_Name', 'User'),
            last_name=user_metadata.get('Last_Name', ''),
            gender=user_metadata.get('Gender', 'M'),
            date_of_birth=user_metadata.get('Date_Of_Birth', ''),
            contact_number=user_metadata.get('Contact_Number', ''),
            email=user_metadata.get('Email', ''),
            data=data
        )
    else:
        app.log.error('[x] BUSINESS ROLE NOT FOUND')
        raise ValueError('business_role')
    return {"result": "true"}

#
# Appointment Block
#
@app.route('/appointments', methods=['POST'], cors=True)
def add_appointment():
    post_body = app.current_request.json_body
    appointment_store = AppointmentStore()
    appointment = appointment_store.add_appointment(
        patient_id=post_body.get('Patient_Id'),
        doctor_id=post_body.get('Doctor_Id'),
        date_start=post_body.get('Start_Date'),
        date_end=post_body.get('End_Date'),
    )
    return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)


@app.route('/appointments', methods=['GET'], cors=True)
def get_appointments():
    appointment_store = AppointmentStore()
    appointments = appointment_store.get_all_appointments()
    return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/appointments/{id}', methods=['GET'], cors=True)
def get_appointment(id):
    appointment_store = AppointmentStore()
    appointment = appointment_store.get_appointment_by_appointment_id(id)
    return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/appointments/patient/{id}', methods=['GET'], cors=True)
def get_appointment(id):
    appointment_store = AppointmentStore()
    appointment = appointment_store.get_appointments_by_patient_id(id)
    return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/appointments/doctor/{id}', methods=['GET'], cors=True)
def get_appointment(id):
    appointment_store = AppointmentStore()
    appointment = appointment_store.get_appointments_by_doctor_id(id)
    return json.dumps(appointment, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/appointments/{id}', methods=['DELETE'], cors=True)
def delete_appointment(id):
    appointment_store = AppointmentStore()
    appointment_store.delete_appointment(id)
    return {"result": "true"}

@app.route('/appointments/upcoming', methods=['GET'], cors=True)
def get_upcoming_appointments():
    appointment_store = AppointmentStore()
    appointments = appointment_store.get_all_upcoming_appointments()
    return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)

@app.route('/appointments/upcoming/doctor/{id}', methods=['GET'], cors=True)
def get_upcoming_appointments_doctor(id):
    appointment_store = AppointmentStore()
    appointments = appointment_store.get_upcoming_appointments_by_doctor_id(id)
    return json.dumps(appointments, cls=recursive_alchemy_encoder(), check_circular=False)