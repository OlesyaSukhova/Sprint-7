from faker import Faker

fake = Faker()

def generate_courier_body():
    return {
        "login": fake.name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

class Url:
    base_url = "https://qa-scooter.praktikum-services.ru"
    courier_url = "/api/v1/courier"
    login_url = "/api/v1/courier/login"
    order_url = "/api/v1/orders"
    delete_url = "/api/v1/courier"


credentials_1 = {
    "firstName": "Олеся",
    "lastName": "Сухова",
    "address": "Петрова, 3",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-02-06",
    "comment": "Привет!",
    "color": [
        "BLACK"
    ]
}

credentials_2 = {
    "firstName": "Олеся",
    "lastName": "Сухова",
    "address": "Петрова, 3",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-02-06",
    "comment": "Привет!",
    "color": [
        "GREY"
    ]
}

credentials_3 = {
    "firstName": "Олеся",
    "lastName": "Сухова",
    "address": "Петрова, 3",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-02-06",
    "comment": "Привет!",
    "color": [
        "GREY",
        "BLACK"
    ]
}

credentials_4 = {
    "firstName": "Олеся",
    "lastName": "Сухова",
    "address": "Петрова, 3",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-02-06",
    "comment": "Привет!",
    "color": []
}


