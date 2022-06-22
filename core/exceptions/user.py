from core.exceptions import CustomException


class NoSuchUserException(CustomException):
    code = 401
    error_code = "USER__USER_DOES_NOT_EXISTS"
    message = "no user was found by id"


class DuplicateEmailException(CustomException):
    code = 400
    error_code = "USER__DUPLICATE_EMAIL"
    message = "duplicate email"


class NotEnoughMoneyBitchException(CustomException):
    code = 400
    error_code = "USER__USER_LOW_BALANCE"
    message = "user's balance is too low :("
