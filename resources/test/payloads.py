register_doctor_payload = {
    "event": "signup",
    "instance_id": "c74c545a-4dff-4d4d-832c-bff8bbe94922",
    "user": {
        "id": "17d5b44c-1472-4445-a9d0-d63dabbe369f",
        "aud": "",
        "role": "",
        "email": "kullen.hatim@lcelandic.com",
        "confirmation_sent_at": "2018-09-05T07:19:47Z",
        "app_metadata": {
            "provider": "email"
        },
        "user_metadata": {
            "Business_Role": "doctor",
            "Contact_Number": "0987654321234567",
            "Date_Of_Birth": "12/01/1993",
            "Email": "kullen.hatim@lcelandic.com",
            "Gender": "F",
            "First_Name": "Test",
            "Full_Name": "Test Test",
            "Last_Name": "Test",
            "address": {
                "Country": "United States",
                "Postcode": "10013",
                "State": "NY",
                "Street": "17 Greenwich St"
            }
        },
        "created_at": "2018-09-05T07:19:47Z",
        "updated_at": "2018-09-05T07:19:47Z"
    }
}

register_receptionist_payload = {
    "event": "signup",
    "instance_id": "c74c545a-4dff-4d4d-832c-bff8bbe94923",
    "user": {
        "id": "17d5b44c-1472-4445-a9d0-d63dabbe3690",
        "aud": "",
        "role": "",
        "email": "kullen.hatim.receptionist@lcelandic.com",
        "confirmation_sent_at": "2018-09-05T07:19:47Z",
        "app_metadata": {
            "provider": "email"
        },
        "user_metadata": {
            "Business_Role": "receptionist",
            "Contact_Number": "0987654321234567",
            "Date_Of_Birth": "12/01/1993",
            "Email": "kullen.hatim.receptionist@lcelandic.com",
            "First_Name": "Test",
            "Gender": "M",
            "Full_Name": "Test Test",
            "Last_Name": "Test",
            "address": {
                "Country": "United States",
                "Postcode": "10013",
                "State": "NY",
                "Street": "17 Greenwich St"
            }
        },
        "created_at": "2018-09-05T07:19:47Z",
        "updated_at": "2018-09-05T07:19:47Z"
    }
}

add_patient_payload = {
    "Contact_Number": "0400000000",
    "Date_Of_Birth": "12/01/1993",
    "Email": "kullen.hatim.patient@lcelandic.com",
    "First_Name": "Test",
    "Gender": "M",
    "Full_Name": "Test Test",
    "Last_Name": "Test",
    "address": {
        "Country": "United States",
        "Postcode": "10013",
        "State": "NY",
        "Street": "17 Greenwich St"
    }
}

update_patient_payload = {
    "AddressId": 3,
    "Contact_Number": "0400000000",
    "Date_Of_Birth": "12/01/1993",
    "Email": "kullen.hatim.patient@lcelandic.com",
    "First_Name": "Updated",
    "Gender": "M",
    "Last_Name": "Test",
    "Patient_Id": 1,
    "address": {
        "AddressId": 3,
        "Country": "Australia",
        "Postcode": 10013,
        "State": "NSW",
        "Street": "17 Greenwich St",
        "Suburb": "",
        "Unit": ""
    }
}

create_medical_case_payload = {
    "Patient_Id" : 1,
    "Medical_Case_Name": "test",
    "Medical_Case_Description": "test",
    "doctors": [
        {
        "AddressId": 3,
        "Contact_Number": "04000000000",
        "Date_Of_Birth": "26/01/1997",
        "Doctor_Id": 13,
        "Email": "patm007@hotmail.com",
        "First_Name": "Patrick",
        "Gender": "M",
        "Last_Name": "Miziewicz",
        "User_Id": "b64bfe4a-ce81-459b-816a-a7cbb24e770d",
        "address": {
            "AddressId": 3,
            "Country": "Australia",
            "Postcode": 2000,
            "State": "NSW",
            "Street": "5 Main St",
            "Suburb": "Castle Hill",
            "Unit": ""
        }
    },
    {
        "AddressId": 6,
        "Contact_Number": "098765432123456",
        "Date_Of_Birth": "12/01/1993",
        "Doctor_Id": 18,
        "Email": "kullen.hatim@lcelandic.com",
        "First_Name": "Test",
        "Gender": "F",
        "Last_Name": "Test",
        "User_Id": "17d5b44c-1472-4445-a9d0-d63dabbe369f",
        "address": {
            "AddressId": 6,
            "Country": "United States",
            "Postcode": 10013,
            "State": "NY",
            "Street": "17 Greenwich St",
            "Suburb": "",
            "Unit": ""
        }
    }
    ]
}

update_medical_case_payload = {
    "Medical_Case_Description": "test",
    "Medical_Case_Id": 1,
    "Medical_Case_Name": "test",
    "Patient_Id": 1,
    "doctors": [
        {
            "AddressId": 1,
            "Contact_Number": "098765432123456",
            "Date_Of_Birth": "12/01/1993",
            "Doctor_Id": 1,
            "Email": "kullen.hatim@lcelandic.com",
            "First_Name": "Test",
            "Gender": "F",
            "Last_Name": "Test",
            "User_Id": "17d5b44c-1472-4445-a9d0-d63dabbe369f",
            "address": {
                "AddressId": 1,
                "Country": "United States",
                "Postcode": 10013,
                "State": "NY",
                "Street": "17 Greenwich St",
                "Suburb": "",
                "Unit": ""
            },
            "medical_cases": []
        }
    ],
    "patient": {
        "AddressId": 1,
        "Contact_Number": "0400000000",
        "Date_Of_Birth": "11/11/1990",
        "Email": "ajsdlakjsd@lakjdlakjdklsa.com",
        "First_Name": "UPDATED1231eqqsdasd",
        "Gender": "F",
        "Last_Name": "TESTaaaaafg",
        "Patient_Id": 1,
        "address": {
            "AddressId": 1,
            "Country": "United States",
            "Postcode": 10010,
            "State": "NY",
            "Street": "12 Lexington Ave",
            "Suburb": "",
            "Unit": ""
        }
    }
}

#
# Appointment Test cases
#
create_appointment_payload = {
        "Patient_Id":1,
        "Doctor_Id":1,
        "Start_Date":"01/02/2019 22:30:00",
        "End_Date":"02/02/2019 23:30:00"
}



