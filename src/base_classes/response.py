from src.enums.global_enums import GlobalErrorMessages
import allure


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    @allure.step('assert_status_code')
    def assert_status_code(self, status_code):
        assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    @allure.step('validate schema')
    def validate(self, schema):
        schema.parse_obj(self.response_json)
        return self
