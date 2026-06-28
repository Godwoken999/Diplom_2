import allure

from api_methods import OrderMethods
from data import ErrorMessages, InvalidData


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией возвращает код 200 и заказ в теле ответа')
    def test_create_order_with_authorization_returns_order(
            self,
            order_payload,
            auth_headers
    ):
        response = OrderMethods.create_order_with_auth(order_payload, auth_headers)
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            'order' in response_body
        ) == (200, True, True)

    @allure.title('Создание заказа без авторизации возвращает код 200 и заказ в теле ответа')
    def test_create_order_without_authorization_returns_order(
            self,
            order_payload
    ):
        response = OrderMethods.create_order(order_payload)
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            'order' in response_body
        ) == (200, True, True)

    @allure.title('Создание заказа с ингредиентами возвращает код 200 и заказ в теле ответа')
    def test_create_order_with_ingredients_returns_order(self, order_payload):
        response = OrderMethods.create_order(order_payload)
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            'order' in response_body
        ) == (200, True, True)

    @allure.title('Создание заказа без ингредиентов возвращает код 400 и текст ошибки')
    def test_create_order_without_ingredients_returns_400_and_error_message(self):
        response = OrderMethods.create_order({'ingredients': []})
        response_body = response.json()

        assert (
            response.status_code,
            response_body['success'],
            response_body['message']
        ) == (
            400,
            False,
            ErrorMessages.INGREDIENTS_REQUIRED
        )

    @allure.title('Создание заказа с неверным хешем ингредиента возвращает код 500 и тело ответа')
    def test_create_order_with_invalid_ingredient_hash_returns_500_and_response_body(
            self
    ):
        response = OrderMethods.create_order({
            'ingredients': [InvalidData.WRONG_INGREDIENT_HASH]
        })

        assert (
            response.status_code,
            bool(response.text)
        ) == (500, True)