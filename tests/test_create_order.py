import allure

from api_methods import OrderMethods
from data import ErrorMessages, InvalidData


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией возвращает код 200')
    def test_create_order_with_authorization_returns_200(
            self,
            order_payload,
            auth_headers
    ):
        response = OrderMethods.create_order_with_auth(order_payload, auth_headers)

        assert response.status_code == 200

    @allure.title('Создание заказа с авторизацией возвращает success true')
    def test_create_order_with_authorization_returns_success_true(
            self,
            order_payload,
            auth_headers
    ):
        response = OrderMethods.create_order_with_auth(order_payload, auth_headers)

        assert response.json()['success'] is True

    @allure.title('Создание заказа без авторизации возвращает код 200')
    def test_create_order_without_authorization_returns_200(self, order_payload):
        response = OrderMethods.create_order(order_payload)

        assert response.status_code == 200

    @allure.title('Создание заказа без авторизации возвращает success true')
    def test_create_order_without_authorization_returns_success_true(
            self,
            order_payload
    ):
        response = OrderMethods.create_order(order_payload)

        assert response.json()['success'] is True

    @allure.title('Создание заказа с ингредиентами возвращает заказ в ответе')
    def test_create_order_with_ingredients_returns_order(self, order_payload):
        response = OrderMethods.create_order(order_payload)

        assert 'order' in response.json()

    @allure.title('Создание заказа без ингредиентов возвращает код 400')
    def test_create_order_without_ingredients_returns_400(self):
        response = OrderMethods.create_order({'ingredients': []})

        assert response.status_code == 400

    @allure.title('Создание заказа без ингредиентов возвращает ошибку Ingredient ids must be provided')
    def test_create_order_without_ingredients_returns_error_message(self):
        response = OrderMethods.create_order({'ingredients': []})

        assert response.json()['message'] == ErrorMessages.INGREDIENTS_REQUIRED

    @allure.title('Создание заказа с неверным хешем ингредиента возвращает код 500')
    def test_create_order_with_invalid_ingredient_hash_returns_500(self):
        response = OrderMethods.create_order({
            'ingredients': [InvalidData.WRONG_INGREDIENT_HASH]
        })

        assert response.status_code == 500