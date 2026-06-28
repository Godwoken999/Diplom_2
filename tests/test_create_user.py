import allure
import pytest

from api_methods import UserMethods
from data import ErrorMessages


@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя возвращает код 200 и success true')
    def test_create_unique_user_returns_200_and_success_true(
            self,
            user_data,
            user_tokens_for_delete
    ):
        response = UserMethods.create_user(user_data)
        response_body = response.json()
        user_tokens_for_delete.append(response_body.get('accessToken'))

        assert (
            response.status_code,
            response_body['success']
        ) == (200, True)

    @allure.title('Создание уже зарегистрированного пользователя возвращает код 403 и текст ошибки')
    def test_create_existing_user_returns_403_and_error_message(
            self,
            user_data,
            user_tokens_for_delete
    ):
        first_response = UserMethods.create_user(user_data)
        first_response_body = first_response.json()
        user_tokens_for_delete.append(first_response_body.get('accessToken'))

        response = UserMethods.create_user(user_data)
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            response_body['message']
        ) == (
            403,
            False,
            ErrorMessages.USER_ALREADY_EXISTS
        )

    @allure.title('Создание пользователя без обязательного поля возвращает код 403 и текст ошибки')
    @pytest.mark.parametrize(
        'field',
        [
            'email',
            'password',
            'name',
        ]
    )
    def test_create_user_without_required_field_returns_403_and_error_message(
            self,
            user_data,
            field
    ):
        payload = user_data.copy()
        payload.pop(field)

        response = UserMethods.create_user(payload)
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            response_body['message']
        ) == (
            403,
            False,
            ErrorMessages.REQUIRED_FIELDS
        )