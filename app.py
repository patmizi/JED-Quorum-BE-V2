import json

from chalice import Chalice
from chalicelib.db.rel_stores import DoctorStore
from chalicelib.lib.encoders import new_alchemy_encoder

app = Chalice(app_name='quorum')
app.debug = True


@app.route('/')
def index():
    return { "Hello": "World" }


@app.route('/doctors/{id}', methods=['GET'], cors=True)
def get_doctor(id):
    print("GOT ID...")
    print(id)
    doctor_store = DoctorStore()

    print("[*] Getting doctor by id...")
    doctor = doctor_store.get_doctor(id)
    print(">> GOT DOCTOR <<")
    print(doctor)
    return json.dumps(doctor, cls=new_alchemy_encoder(), check_circular=False)

@app.route('/doctors', methods=['GET'], cors=True)
def get_doctors():
    print("[*] Get all doctors...")
    doctor_store = DoctorStore()
    doctors = doctor_store.get_all_doctors()
    return json.dumps(doctors, cls=new_alchemy_encoder(), check_circular=False)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @con.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @con.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = con.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
