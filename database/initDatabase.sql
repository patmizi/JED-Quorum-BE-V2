# This script will initialise a quorum db

CREATE TABLE IF NOT EXISTS Address(
  AddressId INT AUTO_INCREMENT,
  Suburb VARCHAR(30) NOT NULL,
  Country VARCHAR(30) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Postcode INT(12) NOT NULL,
  Street VARCHAR(50) NOT NULL,
  Unit VARCHAR(30) NOT NULL,
  PRIMARY KEY (AddressId)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Doctor(
  Doctor_Id INT AUTO_INCREMENT,
  First_Name VARCHAR(30) NOT NULL,
  Last_Name VARCHAR(30) NOT NULL,
  Gender ENUM('M','F') NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Contact_Number VARCHAR(15) NOT NULL,
  Email VARCHAR(50) NOT NULL,
  AddressId INT,
  User_Id VARCHAR(50) NOT NULL,
  FOREIGN KEY (AddressId) REFERENCES Address(AddressId),
  PRIMARY KEY (Doctor_Id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Patient(
  Patient_Id INT AUTO_INCREMENT,
  First_Name VARCHAR(30) NOT NULL,
  Last_Name VARCHAR(30) NOT NULL,
  Gender ENUM('M','F') NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Contact_Number VARCHAR(15) NOT NULL,
  Email VARCHAR(50) NOT NULL,
  AddressId INT,
  FOREIGN KEY (AddressId) REFERENCES Address(AddressId),
  PRIMARY KEY (Patient_Id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Receptionist(
  Receptionist_Id INT AUTO_INCREMENT,
  First_Name VARCHAR(30) NOT NULL,
  Last_Name VARCHAR(30) NOT NULL,
  Gender ENUM('M','F') NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Contact_Number VARCHAR(15) NOT NULL,
  Email VARCHAR(50) NOT NULL,
  AddressId INT,
  User_Id VARCHAR(50) NOT NULL,
  FOREIGN KEY (AddressId) REFERENCES Address(AddressId),
  PRIMARY KEY (Receptionist_Id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS MedicalCase(
  Medical_Case_Id INT AUTO_INCREMENT,
  Patient_Id INT,
  Medical_Case_Name VARCHAR(30) NOT NULL,
  Medical_Case_Description TEXT NOT NULL,
  FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_Id),
  PRIMARY KEY (Medical_Case_Id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS MedicalCaseDoctors(
  Medical_Case_Id INT,
  Doctor_Id INT,
  FOREIGN KEY (Medical_Case_Id) REFERENCES MedicalCase(Medical_Case_Id),
  FOREIGN KEY (Doctor_Id) REFERENCES Doctor(Doctor_Id)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Appointment(
  Appointment_Id INT AUTO_INCREMENT,
  Patient_Id INT,
  Doctor_Id INT,
  Date_Start DATETIME,
  Date_End DATETIME,
  FOREIGN KEY (Patient_Id) REFERENCES Patient(Patient_Id),
  FOREIGN KEY (Doctor_Id) REFERENCES Doctor(Doctor_Id),
  PRIMARY KEY (Appointment_Id)
)ENGINE=InnoDB;



