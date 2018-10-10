import json

responses = {
    "expected_register_doctor": {"result": "true"},
    "expected_register_receptionist": {"result": "true"},
    "expected_get_doctor": [{
        "AddressId": 1,
        "Contact_Number": "0987654321234567",
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
    }],
    "expected_get_receptionist": [{
        "AddressId": 2,
        "Contact_Number": "0987654321234567",
        "Date_Of_Birth": "12/01/1993",
        "Email": "kullen.hatim.receptionist@lcelandic.com",
        "First_Name": "Test",
        "Gender": "M",
        "Last_Name": "Test",
        "Receptionist_Id": 1,
        "User_Id": "17d5b44c-1472-4445-a9d0-d63dabbe3690",
        "address": {
            "AddressId": 2,
            "Country": "United States",
            "Postcode": 10013,
            "State": "NY",
            "Street": "17 Greenwich St",
            "Suburb": "",
            "Unit": ""
        }
    }],
    "expected_add_patient": [{
        "AddressId": 3,
        "Contact_Number": "0400000000",
        "Date_Of_Birth": "12/01/1993",
        "Email": "kullen.hatim.patient@lcelandic.com",
        "First_Name": "Test",
        "Gender": "M",
        "Last_Name": "Test",
        "Patient_Id": 1,
        "address": {
            "AddressId": 3,
            "Country": "United States",
            "Postcode": 10013,
            "State": "NY",
            "Street": "17 Greenwich St",
            "Suburb": "",
            "Unit": ""
        }
    }],
    "expected_update_patient": [{
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
    }],
    "expected_create_medical_case": [{
        "Medical_Case_id": 1,
        "Patient_Id": 1,
        "Medical_Case_Name": "test",
        "Medical_Case_Description": "test"
     }],
    "expected_update_medical_case": [{
        "Medical_Case_Id": 1,
        "Patient_Id": 1,
        "Medical_Case_Name": "updated",
        "Medical_Case_Description": "updated"
    }]

}


def expected_response(key):
    return json.dumps(responses[key])
