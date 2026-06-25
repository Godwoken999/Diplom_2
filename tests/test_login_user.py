import allure

from api_methods import UserMethods
from data import ErrorMessages, InvalidData


@allure.feature('Логин пользователя')
class TestLoginUser:

    @allure.title('При логине существующего пользователя возвращается код 200')
    def test_login_existing_user_returns_200(self, login_response):
        assert login_response.status_code == 200

    @allure.title('При логине существующего пользователя success равен true')
    def test_login_existing_user_returns_success_true(self, login_response):
        assert login_response.json()['success'] is True

    @allure.title('При логине существующего пользователя в ответе есть accessToken')
    def test_login_existing_user_returns_access_token(self, login_response):
        assert 'accessToken' in login_response.json()

    @allure.title('При логине с неверными данными возвращается код 401')
    def test_login_with_invalid_credentials_returns_401(self):
        response = UserMethods.login_user({
            'email': InvalidData.WRONG_EMAIL,
            'password': InvalidData.WRONG_PASSWORD
        })

        assert response.status_code == 401

    @allure.title('При логине с неверными данными возвращается ошибка incorrect')
    def test_login_with_invalid_credentials_returns_error_message(self):
        response = UserMethods.login_user({
            'email': InvalidData.WRONG_EMAIL,
            'password': InvalidData.WRONG_PASSWORD
        })

        assert response.json()['message'] == (
            ErrorMessages.INCORRECT_EMAIL_OR_PASSWORD
        )