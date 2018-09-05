import json

from sqlalchemy.orm import joinedload
from chalicelib.lib.encoders import AlchemyEncoder

from . import DatabaseSession
from .store import MySqlStore
from .entities import Doctor, Address


class DoctorStore(MySqlStore):
    def create_doctor(
            self,
            first_name,
            last_name,
            gender,
            age,
            contact_number,
            email,
            data):
        entity = Doctor(
            First_Name=first_name,
            Last_Name=last_name,
            Gender=gender,
            Age=age,
            Contact_Number=contact_number,
            Email=email,
            **data)

        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

            return self.normalize(entity)

    def get_doctor(self, doctor_id):
        print(doctor_id)
        with DatabaseSession() as session:
            doctor = session.query(Doctor).\
                filter(Doctor.Doctor_Id == doctor_id)
            data = doctor.all()
            if len(data) > 0:
                address = session.query(Address).\
                    filter(Address.AddressId == data[0].AddressId)
                address_data = address.first()
                setattr(data[0], 'address', address_data)

                print("DATA")
                # TODO: Not getting correct output. Possible that encoder is not recursing past surface depth
                print(json.dumps(data, cls=AlchemyEncoder))
            return data


    def get_all_doctors(self):
        with DatabaseSession() as session:
            query = session.query(Doctor)
            data = query.all()
            return data

