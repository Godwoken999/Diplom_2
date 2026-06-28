import allure

from api_methods import UserMethods
from data import ErrorMessages, InvalidData
from helpers import get_user_login_data


@allure.feature('Логин пользователя')
class TestLoginUser:

    @allure.title('Логин существующего пользователя возвращает код 200, success true и accessToken')
    def test_login_existing_user_returns_200_success_true_and_access_token(
            self,
            created_user
    ):
        user_data, _ = created_user

        response = UserMethods.login_user(get_user_login_data(user_data))
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            'accessToken' in response_body
        ) == (200, True, True)

    @allure.title('Логин с неверными данными возвращает код 401 и текст ошибки')
    def test_login_with_invalid_credentials_returns_401_and_error_message(self):
        response = UserMethods.login_user({
            'email': InvalidData.WRONG_EMAIL,
            'password': InvalidData.WRONG_PASSWORD
        })
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            response_body['message']
        ) == (
            401,
            False,
            ErrorMessages.INCORRECT_EMAIL_OR_PASSWORD
        )