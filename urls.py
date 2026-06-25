class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'

    CREATE_USER = f'{BASE_URL}/api/auth/register'
    LOGIN_USER = f'{BASE_URL}/api/auth/login'
    DELETE_USER = f'{BASE_URL}/api/auth/user'

    INGREDIENTS = f'{BASE_URL}/api/ingredients'
    CREATE_ORDER = f'{BASE_URL}/api/orders'