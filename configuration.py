import requests
from global_enums import GlobalErrorMessages

SERVICE_URL = "https://restful-booker.herokuapp.com/booking/"
login = "admin"
password = "password123"
body_post = {
    "firstname": "Test",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
}
body_put = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
    "additionalneeds": "Breakfast",
}


class Response:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert (
                self.response_status in status_code
            ), GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert (
                self.response_status == status_code
            ), GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_len(self, count):
        self.response_json = self.response.json()
        self.response_len = len(self.response_json)
        assert self.response_len == count, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self
