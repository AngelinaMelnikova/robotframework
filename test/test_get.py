import allure
import pytest
from hamcrest import assert_that, is_in

from service.client import RobotFrameworkApi


class TestRobotFramework:

    @allure.title('Проверяем, что сайт открывается в формате html')
    def test_get_robotframework_200(self, robot_framework: RobotFrameworkApi):
        with allure.step('Отправляем запрос на открытие сайта'):
            res_rest = robot_framework.get_robotframework()

        with allure.step('Проверяем, что пришел html'):
            assert_that('b\'<!doctype html>\\n<html>\\n', is_in(str(res_rest.content)))

    @pytest.mark.xfail(reason='Метод отдает 404 ошибку')
    @allure.title('Запрос кодекса поведения роботов')
    def test_get_code_of_conduct_200(self, robot_framework: RobotFrameworkApi):
        with allure.step('Отправляем запрос на открытие кодекса'):
            res_rest = robot_framework.get_code_of_conduct()

        with allure.step('Проверяем, что это кодекс роботов'):
            text = res_rest.text
            assert_that('ROBOT FRAMEWORK CODE OF CONDUCT', is_in(text))

    @allure.title('Открываем список библиотек')
    def test_get_standard_libraries_200(self, robot_framework: RobotFrameworkApi):
        with allure.step('Открываем список библиотек'):
            res_rest = robot_framework.get_standard_libraries()

        with allure.step('Проверяем, что это список библиотек'):
            text = res_rest.text
            assert_that('Standard libraries', is_in(text))

    @allure.title('Запрос определенной версии документации')
    @pytest.mark.parametrize(
        'version',
        ['2.0', '5.0', '3.0.2']
    )
    def test_get_user_guide_200(self, robot_framework: RobotFrameworkApi, version):
        with allure.step('Отправляем запрос на открытие докуметации'):
            res_rest = robot_framework.get_user_guide(version=version)

        with allure.step('Проверяем, что пришел User Guide и версия совпадает с запросом'):
            text = res_rest.text
            assert_that('Robot Framework User Guide', is_in(text))
            assert_that(f'Version {version}', is_in(text))

    @allure.title('Запрос последней версии документации')
    def test_get_user_guide_latest_version_200(self, robot_framework: RobotFrameworkApi):
        with allure.step('Отправляем запрос на открытие докуметации'):
            res_rest = robot_framework.get_user_guide(version='latest')

        with allure.step('Проверяем, что это User Guide'):
            text = res_rest.text
            assert_that('Robot Framework User Guide', is_in(text))
