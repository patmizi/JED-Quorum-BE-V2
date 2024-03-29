from chalicelib.lib import helpers
from datetime import datetime
from chalicelib.lib.exceptions import NotFoundException

from . import DatabaseSession
from .store import MySqlStore
from .entities import Doctor, Receptionist, Patient, Address, MedicalCase, Appointment


class DoctorStore(MySqlStore):
    def create_doctor(self, first_name, last_name, gender, date_of_birth, contact_number, email, data):
        date_of_birth = helpers.get_date_from_string(date_of_birth)
        entity = Doctor(
            First_Name=first_name,
            Last_Name=last_name,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Gender=gender,
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
            Gender=gender,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Email=email,
            **data)
        if 'address' in data:
            entity.address = Address(
                Suburb=data['address'].get('Suburb', ""),
                Country=data['address'].get('Country', ""),
                State=data['address'].get('State', ""),
                Postcode=data['address'].get('Postcode', ""),
                Street=data['address'].get('Street', ""),
                Unit=data['address'].get('Unit', "")
            )

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
            patients = session.query(Patient).all()
            for patient in patients:
                patient.cases = []
                cases = session.query(MedicalCase). \
                    filter(MedicalCase.Patient_Id == patient.Patient_Id). \
                    all()
                if cases is not None:
                    patient.cases = cases
            return patients

    def get_patient(self, patient_id):
        with DatabaseSession() as session:
            patient = session.query(Patient).get(patient_id)
            patient.cases = []
            cases = session.query(MedicalCase). \
                filter(MedicalCase.Patient_Id == patient_id). \
                all()
            if cases is not None:
                patient.cases = cases
            return patient

    def add_patient(self, first_name, last_name, gender, date_of_birth, contact_number, email, data):
        date_of_birth = helpers.get_date_from_string(date_of_birth)
        entity = Patient(
            First_Name=first_name,
            Last_Name=last_name,
            Gender=gender,
            Date_Of_Birth=date_of_birth,
            Contact_Number=contact_number,
            Email=email,
            **data)
        if 'address' in data:
            entity.address = Address(
                Suburb=data['address'].get('Suburb', ""),
                Country=data['address'].get('Country', ""),
                State=data['address'].get('State', ""),
                Postcode=data['address'].get('Postcode', ""),
                Street=data['address'].get('Street', ""),
                Unit=data['address'].get('Unit', "")
            )

        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()
            return self.get_patient(entity.Patient_Id)

    def update_patient(self, patient_id, params):
        self.update_object(entity=Patient, _id=patient_id, params=params)
        return self.get_patient(patient_id)

    def delete_patient(self, patient_id):
        with DatabaseSession() as session:
            session.query(Patient).filter(Patient.Patient_Id == patient_id).delete()
            session.flush()
            session.commit()


class MedicalCaseStore(MySqlStore):
    def get_medical_case(self, medical_case_id):
        with DatabaseSession() as session:
            query = session.query(MedicalCase). \
                filter(MedicalCase.Medical_Case_Id == medical_case_id)
            data = query.first()
            return data

    def add_medical_case(self, medical_case_name, medical_case_description, patient_id, data):
        case = MedicalCase(
            Medical_Case_Name=medical_case_name,
            Medical_Case_Description=medical_case_description,
            Patient_Id=patient_id
        )
        with DatabaseSession() as session:
            if data.get('doctors') is not None:
                case.doctors = []
                for doc in data.get('doctors'):
                    doctor = session.query(Doctor).get(doc.get('Doctor_Id'))
                    # We can handle errors here too
                    if doctor:
                        case.doctors.append(doctor)
            session.add(case)
            session.flush()
            session.commit()

            return self.get_medical_case(case.Medical_Case_Id)

    def update_medical_case(self, medical_case_id, medical_case_name, medical_case_description, patient_id, data):
        with DatabaseSession() as session:
            case = session.query(MedicalCase).get(medical_case_id)
            if not case:
                raise NotFoundException()
            case.Medical_Case_Name = medical_case_name
            case.Medical_Case_Description = medical_case_description
            patient = session.query(Patient).get(patient_id)
            if not patient:
                raise NotFoundException()
            if data.get('doctors') is not None:
                case.doctors = []
                for doc in data.get('doctors'):
                    doctor = session.query(Doctor).get(doc.get('Doctor_Id'))
                    if doctor:
                        case.doctors.append(doctor)
            session.commit()
        return self.get_medical_case(medical_case_id)


class AppointmentStore(MySqlStore):
    def get_appointments_by_patient_id(self, patient_id):
        with DatabaseSession() as session:
            query = session.query(Appointment). \
                filter(Appointment.Patient_Id == patient_id)
            data = query.all()
            return data

    def get_appointments_by_doctor_id(self, doctor_id):
        with DatabaseSession() as session:
            query = session.query(Appointment). \
                filter(Appointment.Doctor_Id == doctor_id)
            data = query.all()
            return data

    def get_appointment_by_appointment_id(self, appointment_id):
        with DatabaseSession() as session:
            query = session.query(Appointment). \
                filter(Appointment.Appointment_Id == appointment_id)
            data = query.all()
            return data

    def get_all_appointments(self):
        with DatabaseSession() as session:
            query = session.query(Appointment)
            data = query.all()
            return data

    def get_all_upcoming_appointments(self):
        c_time = datetime.now()
        with DatabaseSession() as session:
            query = session.query(Appointment).filter(Appointment.Date_Start >= c_time)
            data = query.all()
            return data

    def get_upcoming_appointments_by_doctor_id(self, doctor_id):
        c_time = datetime.now()
        with DatabaseSession() as session:
            query = session.query(Appointment).filter(Appointment.Doctor_Id == doctor_id
                                                      and Appointment.Date_Start >= c_time)
            data = query.all()
            return data

    def delete_appointment(self, appointment_id):
        print(datetime.now())
        with DatabaseSession() as session:
            session.query(Appointment).filter(Appointment.Appointment_Id == appointment_id).delete()
            session.flush()
            session.commit()

    def add_appointment(self, patient_id, doctor_id, date_start, date_end):
        date_start = helpers.get_datetime_from_string(date_start)
        date_end = helpers.get_datetime_from_string(date_end)
        entity = Appointment(
            Date_Start=date_start,
            Date_End=date_end,
            Patient_Id=patient_id,
            Doctor_Id=doctor_id
        )
        with DatabaseSession() as session:
            session.add(entity)
            session.flush()
            session.commit()

        return self.get_appointment_by_appointment_id(appointment_id=entity.Appointment_Id)
