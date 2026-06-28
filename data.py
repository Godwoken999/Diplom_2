class UserData:
    PASSWORD = 'password123'
    NAME = 'Vladimir'


class ErrorMessages:
    USER_ALREADY_EXISTS = 'User already exists'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    INCORRECT_EMAIL_OR_PASSWORD = 'email or password are incorrect'
    INGREDIENTS_REQUIRED = 'Ingredient ids must be provided'


class InvalidData:
    WRONG_EMAIL = 'wrong_email@test.ru'
    WRONG_PASSWORD = 'wrong_password'
    WRONG_INGREDIENT_HASH = 'wrong_ingredient_hash'