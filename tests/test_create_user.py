import allure
import pytest

from api_methods import UserMethods
from data import ErrorMessages


@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('При создании уникального пользователя возвращается код 200')
    def test_create_unique_user_returns_200(self, created_user_response):
        response, _ = created_user_response

        assert response.status_code == 200

    @allure.title('При создании уникального пользователя success равен true')
    def test_create_unique_user_returns_success_true(self, created_user_response):
        response, _ = created_user_response

        assert response.json()['success'] is True

    @allure.title('При создании уникального пользователя в ответе есть accessToken')
    def test_create_unique_user_returns_access_token(self, created_user_response):
        response, _ = created_user_response

        assert 'accessToken' in response.json()

    @allure.title('При повторном создании пользователя возвращается код 403')
    def test_create_existing_user_returns_403(self, created_user):
        user_data, _ = created_user

        response = UserMethods.create_user(user_data)

        assert response.status_code == 403

    @allure.title('При повторном создании пользователя возвращается ошибка User already exists')
    def test_create_existing_user_returns_user_already_exists_message(
            self,
            created_user
    ):
        user_data, _ = created_user

        response = UserMethods.create_user(user_data)

        assert response.json()['message'] == ErrorMessages.USER_ALREADY_EXISTS

    @allure.title('При создании пользователя без обязательного поля возвращается код 403')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_required_field_returns_403(
            self,
            user_data,
            field
    ):
        user_data.pop(field)

        response = UserMethods.create_user(user_data)

        assert response.status_code == 403

    @allure.title('При создании пользователя без обязательного поля возвращается ошибка required fields')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_required_field_returns_required_fields_message(
            self,
            user_data,
            field
    ):
        user_data.pop(field)

        response = UserMethods.create_user(user_data)

        assert response.json()['message'] == ErrorMessages.REQUIRED_FIELDS