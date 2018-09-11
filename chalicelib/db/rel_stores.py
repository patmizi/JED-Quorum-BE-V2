import json
import datetime

from sqlalchemy.orm import joinedload

from chalicelib.lib import helpers
from chalicelib.lib.encoders import new_alchemy_encoder

from . import DatabaseSession
from .store import MySqlStore
from .entities import Doctor, Receptionist


class DoctorStore(MySqlStore):
    def create_doctor(self, first_name, last_name, gender, date_of_birth, contact_number, email, data):
        date_of_birth = helpers.get_date_from_string(date_of_birth)
        entity = Doctor(
            First_Name=first_name,
            Last_Name=last_name,
            # Gender=gender,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Email=email,
            **data)

        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

            return self.get_doctor(entity.Doctor_Id)

    def get_doctor(self, doctor_id):
        print(doctor_id)
        with DatabaseSession() as session:
            doctor = session.query(Doctor).\
                filter(Doctor.Doctor_Id == doctor_id)
            data = doctor.all()
            return data


    def get_all_doctors(self):
        with DatabaseSession() as session:
            query = session.query(Doctor)
            data = query.all()
            return data


class ReceptionistStore(MySqlStore):
    def create_receptionist(self, first_name, last_name, gender, date_of_birth, contact_number, email, data):
        date_of_birth = helpers.get_date_from_string(date_of_birth)
        entity = Receptionist(
            First_Name=first_name,
            Last_Name=last_name,
            # Gender=gender,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Email=email,
            **data)

        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

            return "DONE"
