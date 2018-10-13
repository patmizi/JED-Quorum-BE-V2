CREATE TABLE IF NOT EXISTS Address (
  AddressId integer primary key,
  Suburb text NOT NULL,
  Country text NOT NULL,
  State text NOT NULL,
  Postcode integer NOT NULL,
  Street text NOT NULL,
  Unit text NOT NULL
);

CREATE TABLE IF NOT EXISTS Doctor (
  Doctor_Id integer primary key,
  First_Name text NOT NULL,
  Last_Name text NOT NULL,
  Gender text NOT NULL,
  Date_Of_Birth date NOT NULL,
  Contact_Number text NOT NULL,
  Email text NOT NULL,
  AddressId integer,
  User_Id text NOT NULL
);

CREATE TABLE IF NOT EXISTS Patient (
  Patient_Id integer primary key,
  First_Name text NOT NULL,
  Last_Name text NOT NULL,
  Gender text NOT NULL,
  Date_Of_Birth date NOT NULL,
  Contact_Number text NOT NULL,
  Email text NOT NULL,
  AddressId integer
);

CREATE TABLE IF NOT EXISTS Receptionist (
  Receptionist_Id integer primary key,
  First_Name text NOT NULL,
  Last_Name text NOT NULL,
  Gender text NOT NULL,
  Date_Of_Birth date NOT NULL,
  Contact_Number text NOT NULL,
  Email text NOT NULL,
  AddressId integer,
  User_Id text NOT NULL
);

CREATE TABLE IF NOT EXISTS MedicalCase (
  Medical_Case_Id integer primary key,
  Patient_Id integer NOT NULL,
  Medical_Case_Name text NOT NULL,
  Medical_Case_Description text NOT NULL
);

CREATE TABLE IF NOT EXISTS MedicalCaseDoctors (
  Medical_Case_Id integer primary key,
  Doctor_Id integer primary key
);

CREATE TABLE IF NOT EXISTS Appointment (
  Appointment_Id integer primary key,
  Patient_Id integer NOT NULL,
  Doctor_Id integer NOT NULL,
  Date_Start datetime NOT NULL,
  Date_End datetime
);