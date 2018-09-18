import json

from chalice import Chalice
from chalicelib.db.rel_stores import DoctorStore, ReceptionistStore
from chalicelib.lib.encoders import recursive_alchemy_encoder

app = Chalice(app_name='quorum')
app.debug = True


@app.route('/')
def index():
    return {"Hello": "World"}


@app.route('/doctors/{id}', methods=['GET'], cors=True)
def get_doctor(id):
    doctor_store = DoctorStore()
    doctor = doctor_store.get_doctor(id)
    print(doctor)
    return json.dumps(doctor, cls=recursive_alchemy_encoder(), check_circular=False)



@app.route('/doctors', methods=['GET'], cors=True)
def get_doctors():
    print("[*] Get all doctors...")
    doctor_store = DoctorStore()
    doctors = doctor_store.get_all_doctors()
    return json.dumps(doctors, cls=recursive_alchemy_encoder(), check_circular=False)



@app.route('/receptionists/{id}')
def get_receptionist(id):
    receptionist_store = ReceptionistStore()
    receptionist = receptionist_store.get_receptionist(id)
    print(receptionist)
    return json.dumps(receptionist, cls=recursive_alchemy_encoder(), check_circular=False)


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
        data['address'] = user_metadata['address']

    if user_metadata['business_role'] == 'doctor':
        app.log.info('Registering a doctor...')
        doctor_store = DoctorStore()
        doctor_store.create_doctor(
            first_name=user_metadata['first_name'],
            last_name=user_metadata['last_name'],
            gender="M",
            date_of_birth=user_metadata['date_of_birth'],
            contact_number=user_metadata['contact_number'],
            email=user_metadata['email'],
            data=data
        )
    elif user_metadata['business_role'] == 'receptionist':
        app.log.info('Registering a receptionist')
        receptionist_store = ReceptionistStore()
        receptionist_store.create_receptionist(
            first_name=user_metadata['first_name'],
            last_name=user_metadata['last_name'],
            gender="M",
            date_of_birth=user_metadata['date_of_birth'],
            contact_number=user_metadata['contact_number'],
            email=user_metadata['email'],
            data={
                "User_Id": user_json['user']['id']
            }
        )
    else:
        app.log.error('[x] BUSINESS ROLE NOT FOUND')
        raise ValueError('business_role')
    return {"result": "true"}
