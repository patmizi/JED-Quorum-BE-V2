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
        "doctors": "1"       
}

update_medical_case_payload = {
        "Medical_Case_id": 1,
        "Patient_Id" : 1,
        "Medical_Case_Name": "updated",
        "Medical_Case_Description": "updated"
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

