from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Address(Base):
    __tablename__ = "Address"
    pass

class Appointment(Base):
    __tablename__ = "Appointment"
    pass

class Doctor(Base):
    __tablename__ = "Doctor"
    pass

class MedicalCase(Base):
    __tablename__ = "MedicalCase"
    pass

class MedicalCaseDoctors(Base):
    __tablename__ = "MedicalCaseDoctors"
    pass

class Patient(Base):
    __tablename__ = "Patient"
    pass

class Receptionist(Base):
    __tablename__ = "Receptionist"
    pass

