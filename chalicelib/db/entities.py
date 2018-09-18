from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

MedicalCaseDoctors = Table(
    'association',
    Base.metadata,
    Column('Medical_Case_Id', Integer, ForeignKey('MedicalCase.Medical_Case_Id')),
    Column('Doctor_Id', Integer, ForeignKey('Doctor.Doctor_Id'))
)


class Address(Base):
    __tablename__ = "Address"

    AddressId = Column(Integer, primary_key=True)
    Suburb = Column(String(30), nullable=False)
    Country = Column(String(30), nullable=False)
    State = Column(String(15), nullable=False)
    Postcode = Column(Integer, nullable=False)
    Street = Column(String(50), nullable=False)
    Unit = Column(String(30), nullable=False)


# class Appointment(Base):
#     __tablename__ = "Appointment"
#     pass

class Doctor(Base):
    __tablename__ = "Doctor"

    Doctor_Id = Column(Integer, primary_key=True)
    First_Name = Column(String(30), nullable=False)
    Last_Name = Column(String(30), nullable=False)
    Gender = Column(String(2), nullable=False)
    Date_Of_Birth = Column(Date, nullable=False)
    Contact_Number = Column(String(15), nullable=False)
    Email = Column(String(50), nullable=False)
    AddressId = Column(ForeignKey('Address.AddressId', ondelete='CASCADE'), index=True)
    User_Id = Column(String(50), nullable=False)

    medical_cases = relationship('MedicalCase', secondary=MedicalCaseDoctors)
    address = relationship('Address', lazy="joined")


class MedicalCase(Base):
    __tablename__ = "MedicalCase"

    Medical_Case_Id = Column(Integer, primary_key=True)
    Medical_Case_Name = Column(String(30), nullable=False)
    Medical_Case_Description = Column(Text, nullable=False)

    patient = relationship("Patient", lazy="joined")
    doctors = relationship('Doctor', secondary=MedicalCaseDoctors)


class Patient(Base):
    __tablename__ = "Patient"

    Patient_Id = Column(Integer, primary_key=True)
    First_Name = Column(String(30), nullable=False)
    Last_Name = Column(String(30), nullable=False)
    Gender = Column(String(2), nullable=False)
    Date_Of_Birth = Column(Date, nullable=False)
    Contact_Number = Column(String(15), nullable=False)
    Email = Column(String(50), nullable=False)
    Address_Id = Column(ForeignKey('Address.AddressId', ondelete='CASCADE'), index=True)

    address = relationship('Address', lazy="joined")


class Receptionist(Base):
    __tablename__ = "Receptionist"

    Receptionist_Id = Column(Integer, primary_key=True)
    First_Name = Column(String(30), nullable=False)
    Last_Name = Column(String(30), nullable=False)
    Gender = Column(String(2), nullable=False)
    Date_Of_Birth = Column(Date, nullable=False)
    Contact_Number = Column(String(15), nullable=False)
    Email = Column(String(50), nullable=False)
    AddressId = Column(ForeignKey('Address.AddressId', ondelete='CASCADE'), index=True)
    User_Id = Column(String(50), nullable=False)

    address = relationship('Address', lazy="joined")
