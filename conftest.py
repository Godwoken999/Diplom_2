import pytest

from api_methods import IngredientMethods, UserMethods
from helpers import (
    generate_unique_user_data,
    get_auth_headers,
    get_user_login_data
)


@pytest.fixture
def user_data():
    return generate_unique_user_data()


@pytest.fixture
def created_user(user_data):
    create_response = UserMethods.create_user(user_data)
    access_token = create_response.json().get('accessToken')

    yield user_data, access_token

    if access_token:
        UserMethods.delete_user(get_auth_headers(access_token))


@pytest.fixture
def created_user_response(user_data):
    create_response = UserMethods.create_user(user_data)
    access_token = create_response.json().get('accessToken')

    yield create_response, user_data

    if access_token:
        UserMethods.delete_user(get_auth_headers(access_token))


@pytest.fixture
def login_response(created_user):
    user_data, _ = created_user

    return UserMethods.login_user(get_user_login_data(user_data))


@pytest.fixture
def ingredient_ids():
    response = IngredientMethods.get_ingredients()
    ingredients = response.json()['data']

    return [
        ingredients[0]['_id'],
        ingredients[1]['_id']
    ]


@pytest.fixture
def order_payload(ingredient_ids):
    return {
        'ingredients': ingredient_ids
    }


@pytest.fixture
def auth_headers(created_user):
    _, access_token = created_user

    return get_auth_headers(access_token)