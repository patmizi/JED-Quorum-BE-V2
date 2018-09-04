import json

from chalice import Chalice
from db.orm import DoctorStore

app = Chalice(app_name='quorum')

@app.route('/')
def index():
    return { "Hello": "World" }

@app.route('/doctors/{id}')
def get_doctor(id):
    print("GOT ID...")
    print(id)

    doctor_store = DoctorStore()
    doctor_id = 1

    print("[*] Getting doctor by id...")
    doctor = doctor_store.get_doctor(doctor_id)
    print(">> GOT DOCTOR <<")
    print(doctor)
    return json.dumps(doctor)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
