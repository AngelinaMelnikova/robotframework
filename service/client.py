import allure
import requests
from hamcrest import equal_to, assert_that


class RobotFrameworkApi:
    host = None

    def __init__(self, verify: bool = False):
        self._session = requests.session()
        self._session.verify = verify

    def _send_request(self, method: str, path: str, **kwargs):
        url = f'{self.host}{path}'
        response = self._session.request(method=method, url=url, **kwargs)

        return response

    @allure.step('Проверяем, что сайт открылся успешно')
    def get_robotframework(self, status_code=200):
        response = self._send_request('get', '/robotframework/')
        assert_that(response.status_code, equal_to(status_code))

        return response

    @allure.step('Проверяем, что документация открылась успешно')
    def get_user_guide(self, version, status_code=200):
        response = self._send_request('get', f'/robotframework/{version}/RobotFrameworkUserGuide.html')
        assert_that(response.status_code, equal_to(status_code))

        return response

    @allure.step('Проверяем, что кодекс открылся успешно')
    def get_code_of_conduct(self, status_code=200):
        response = self._send_request('get', '/code-of-conduct')
        assert_that(response.status_code, equal_to(status_code))

        return response

    @allure.step('Проверяем, что список библиотек открылся успешно')
    def get_standard_libraries(self, status_code=200):
        response = self._send_request('get', '/robotframework/#standard-libraries')
        assert_that(response.status_code, equal_to(status_code))

        return response
