import uuid

from data import UserData


def generate_unique_user_data():
    unique_part = uuid.uuid4().hex

    return {
        'email': f'test_{unique_part}@yandex.ru',
        'password': UserData.PASSWORD,
        'name': UserData.NAME
    }


def get_user_login_data(user_data):
    return {
        'email': user_data['email'],
        'password': user_data['password']
    }


def get_auth_headers(access_token):
    return {
        'Authorization': access_token
    }