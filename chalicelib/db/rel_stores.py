from . import DatabaseSession
from .store import MySqlStore
from .entities import Doctor


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
        print("DOCTOR ID TO QUERY")
        print(doctor_id)
        with DatabaseSession() as session:
            print("CREATED SESSION. WE GUCCI")
            query = session.query(Doctor).filter(Doctor.Doctor_Id == doctor_id)
            print("DOES IT BREAK HERE???")
            print(query)
            data = query.all()
            print("DATA")
            print(query)
            return data
