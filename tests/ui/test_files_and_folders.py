import allure
import pytest
from allure_commons.types import AttachmentType
from generator.generator import generated_folder_name, generated_file_name


@pytest.mark.ui
@pytest.mark.regression
@allure.epic('UI Яндекс.Диск')
@allure.story('Операции над файлами и папками')
class TestOperationsOnFolders:

    @pytest.mark.smoke
    @allure.testcase('https://...')
    @allure.title('Создание файла')
    @allure.severity('blocker')
    def test_file_create(self, app):
        folder = next(generated_folder_name())
        file = next(generated_file_name())
        app.home.open_page('disk')
        app.disk.create('folder', folder.name)
        app.disk.open(folder.name)
        current_count_files = app.disk.get_count_files()
        app.disk.create('file', file.name)
        app.disk.file_close()
        result_count_files, name_files = app.disk.get_count_files()
        with allure.step('Проверяем факт создания файла'):
            allure.attach(app.wd.get_screenshot_as_png(), name='Text', attachment_type=AttachmentType.PNG)
            assert current_count_files == result_count_files - 1, 'Recieved count files is not equal to expected'
        with allure.step('Проверяем наименование файла'):
            assert file.name in name_files, 'Recieved name file is not equal to expected'

    @pytest.mark.smoke
    @allure.testcase('https://...')
    @allure.title('Загрузка файла')
    @allure.severity('blocker')
    def test_file_upload(self, app):
        folder = next(generated_folder_name())
        app.home.open_page('disk')
        app.disk.create('folder', folder.name)
        app.disk.open(folder.name)
        file_name, text = app.disk.upload_file()
        app.disk.open(file_name)
        with allure.step('Проверяем текст в файле'):
            allure.attach(app.wd.get_screenshot_as_png(), name='Text', attachment_type=AttachmentType.PNG)
            assert app.disk.get_text_file_txt() == text, 'Received file content is not as expected'
        app.disk.file_close()
