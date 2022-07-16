import json
import allure
import pytest
import requests
from src.schemas.files_and_folders import CreateFolder
from generator.generator import generated_folder_name
from src.base_classes.response import Response


@pytest.mark.api
@pytest.mark.regression
@allure.epic('API Яндекс.Диск')
@allure.story('Операции над файлами и папками')
class TestOperationsOnFolders:
    config_json = json.load(open(r"C:\Users\penko\PycharmProjects\yandex_disk\target.json"))
    BASE_URL = config_json['api']['base_url']
    TOKEN = config_json['api']['token']

    @pytest.mark.smoke
    @allure.testcase('https://...')
    @allure.title('Создание папки')
    @allure.severity('blocker')
    def test_folder_create(self):
        folder = next(generated_folder_name())
        url = f'{self.BASE_URL}/disk/resources?path=%2F{folder.name}'
        headers = {'Authorization': f'OAuth {self.TOKEN}'}
        resp_folder_create = requests.put(url=url, headers=headers)
        with allure.step('Проверяем соответствие кода и тела ответа'):
            response = Response(resp_folder_create)
            response.assert_status_code(201).validate(CreateFolder)
        with allure.step('Проверяем успешное создание папки'):
            resp_check_folder = requests.get(url=resp_folder_create.json()['href'], headers=headers)
            assert folder.name == resp_check_folder.json()['name'], 'Recieved name is not equal to expected'
        with allure.step('Удаляем созданную папку'):
            requests.delete(url=f'https://cloud-api.yandex.net/v1/disk/resources?path=%2F{folder.name}',
                            headers=headers)

    @allure.testcase('https://...')
    @allure.title('Параметризованный тест (для примера)')
    @allure.severity('medium')
    @pytest.mark.parametrize('url, code', [('/disk/', 200),
                                           ('/diskk/', 404)])
    def test_user_drive_data(self, url, code):
        url = f'{self.BASE_URL}{url}'
        headers = {'Authorization': f'OAuth {self.TOKEN}'}
        response = Response(requests.get(url=url, headers=headers))
        response.assert_status_code(code)

    @pytest.mark.skip
    @allure.testcase('https://...')
    @allure.title('Пропущенный тест (для примера)')
    @allure.severity('minor')
    def test_skip(self):
        pass
