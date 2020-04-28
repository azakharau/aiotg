class FunctionNotAllowed(Exception):
    ...


class TelegramBaseException(Exception):
    ...


class TelegramAPIException(TelegramBaseException):
    ...


class TelegramDataObjectException(TelegramBaseException):
    ...


class HandlerException(TelegramBaseException):
    ...


class HandlerCloseException(TelegramBaseException):
    ...


class DispatcherException(TelegramBaseException):
    ...
