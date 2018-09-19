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
    }]
}


def expected_response(key):
    return json.dumps(responses[key])