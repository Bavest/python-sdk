from datetime import datetime


class BavestApiStatusException(Exception):
    statuscode = None
    body = None

    def __init__(self, api_exception):
        self.statuscode = api_exception['statusCode']
        self.body = api_exception['body']


class BavestApiException(Exception):
    errorMessage = None
    errorType = None
    requestId = None
    stackTrace = None

    def __init__(self, api_exception):
        self.errorMessage = api_exception['errorMessage']
        self.errorType = api_exception['errorType']
        self.requestId = api_exception['requestId']
        self.stackTrace = api_exception['stackTrace']


class BavestInvalidTypeError(BavestApiException):
    def __init__(self, api_exception):
        super().__init__(api_exception)
        print("Invalid Data type: ", self.errorMessage)


class BavestInvalidQueryError(BavestApiStatusException):
    def __init__(self, api_exception):
        super().__init__(api_exception)
        print("Invalid Query: ", self.body)


class BavestAuthenticationError(BavestApiException):
    ...


class BavestApiError(BavestApiException):
    ...


def check_response(content):
    if "errorType" in content:
        raise BavestInvalidTypeError(content)
    elif "statusCode" in content:
        if content["statusCode"] == 400:
            raise BavestInvalidQueryError(content)
        else:
            return content
    elif "message" in content:
        if content["message"] == "Forbidden":
            print("Invalid API key")
    else:
        return content
