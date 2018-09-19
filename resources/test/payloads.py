

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
            "business_role": "doctor",
            "contact_number": "0987654321234567",
            "date_of_birth": "12/01/1993",
            "email": "kullen.hatim@lcelandic.com",
            "gender": "F",
            "first_name": "Test",
            "full_name": "Test Test",
            "last_name": "Test",
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
            "business_role": "receptionist",
            "contact_number": "0987654321234567",
            "date_of_birth": "12/01/1993",
            "email": "kullen.hatim.receptionist@lcelandic.com",
            "first_name": "Test",
            "gender": "M",
            "full_name": "Test Test",
            "last_name": "Test",
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
    "contact_number": "0400000000",
    "date_of_birth": "12/01/1993",
    "email": "kullen.hatim.patient@lcelandic.com",
    "first_name": "Test",
    "gender": "M",
    "full_name": "Test Test",
    "last_name": "Test",
    "address": {
        "Country": "United States",
        "Postcode": "10013",
        "State": "NY",
        "Street": "17 Greenwich St"
    }
}