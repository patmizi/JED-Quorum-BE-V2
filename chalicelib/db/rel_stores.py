from chalicelib.lib import helpers

from . import DatabaseSession
from .store import MySqlStore
from .entities import Doctor, Receptionist, Patient, Address, MedicalCase


class DoctorStore(MySqlStore):
    def create_doctor(self, first_name, last_name, gender, date_of_birth, contact_number, email, data):
        date_of_birth = helpers.get_date_from_string(date_of_birth)
        entity = Doctor(
            First_Name=first_name,
            Last_Name=last_name,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Email=email,
            **data)
        if 'address' in data:
            address_entity = Address(
                Suburb=data['address'].get('Suburb', ""),
                Country=data['address'].get('Country', ""),
                State=data['address'].get('State', ""),
                Postcode=data['address'].get('Postcode', ""),
                Street=data['address'].get('Street', ""),
                Unit=data['address'].get('Unit', "")
            )
            entity.address = address_entity
        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

            return self.get_doctor(entity.Doctor_Id)

    def get_doctor(self, doctor_id):
        print(doctor_id)
        with DatabaseSession() as session:
            doctor = session.query(Doctor). \
                filter(Doctor.Doctor_Id == doctor_id)
            data = doctor.all()
            return data

    def get_all_doctors(self):
        with DatabaseSession() as session:
            query = session.query(Doctor)
            data = query.all()
            return data

    def update_doctor(self, doctor_id, params):
        self.update_object(entity=Doctor, _id=doctor_id, params=params)
        return self.get_doctor(doctor_id)


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
        if 'address' in data:
            address_entity = Address(
                Suburb=data['address'].get('Suburb', ""),
                Country=data['address'].get('Country', ""),
                State=data['address'].get('State', ""),
                Postcode=data['address'].get('Postcode', ""),
                Street=data['address'].get('Street', ""),
                Unit=data['address'].get('Unit', "")
            )
            entity.address = address_entity
        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

            return self.get_receptionist(entity.Receptionist_Id)

    def get_receptionist(self, receptionist_id):
        print(receptionist_id)
        with DatabaseSession() as session:
            receptionist = session.query(Receptionist). \
                filter(Receptionist.Receptionist_Id == receptionist_id)
            data = receptionist.all()
            return data

    def get_all_receptionists(self):
        with DatabaseSession() as session:
            query = session.query(Receptionist)
            data = query.all()
            return data

    def update_receptionist(self, receptionist_id, params):
        self.update_object(entity=Receptionist, _id=receptionist_id, params=params)
        return self.get_receptionist(receptionist_id)

class PatientStore(MySqlStore):
    def get_all_patients(self):
        with DatabaseSession() as session:
            query = session.query(Patient)
            data = query.all()
            return data

    def get_patient(self, patient_id):
        with DatabaseSession() as session:
            query = session.query(Patient).\
                filter(Patient.Patient_Id == patient_id)
            data = query.all()
            return data

class MedicalCaseStore(MySqlStore):
    def get_medical_case(self, medical_case_id):
        with DatabaseSession() as session:
            query = session.query(MedicalCase). \
                filter(MedicalCase.Medical_Case_Id == medical_case_id)
            data = query.all()
            return data

    def add_medical_case(self, medical_case_name, medical_case_description, patient_data, data):
        case = MedicalCase(
            Medical_Case_Name=medical_case_name,
            Medical_Case_Description=medical_case_description
        )
        case.patient = Patient(
            Patient_Id=patient_data.get('Patient_Id'),
        )
        if data.get('doctors') is not None:
            case.doctors = []
            for d in data.get('doctors'):
                case.doctors.append(
                    Doctor(
                        Doctor_Id=d.get('Doctor_Id')
                    )
                )
        with DatabaseSession() as session:
            session.add(case)
            session.flush()
            session.commit()

            return self.get_medical_case(case.Medical_Case_Id)
