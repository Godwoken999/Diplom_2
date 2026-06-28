import allure
import requests

from urls import Urls


class UserMethods:

    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(payload):
        return requests.post(Urls.CREATE_USER, json=payload)

    @staticmethod
    @allure.step('Авторизоваться пользователем')
    def login_user(payload):
        return requests.post(Urls.LOGIN_USER, json=payload)

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(headers):
        return requests.delete(Urls.DELETE_USER, headers=headers)


class IngredientMethods:

    @staticmethod
    @allure.step('Получить список ингредиентов')
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)


class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ без авторизации')
    def create_order(payload):
        return requests.post(Urls.CREATE_ORDER, json=payload)

    @staticmethod
    @allure.step('Создать заказ с авторизацией')
    def create_order_with_auth(payload, headers):
        return requests.post(
            Urls.CREATE_ORDER,
            json=payload,
            headers=headers
        )