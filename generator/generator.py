import os
import random
from data.data import Folder, File
from faker import Faker

fake_en = Faker('En')


def generated_folder_name():
    yield Folder(
        name=f'test_folder_{fake_en.name()}_{random.randint(0, 10)}'
    )


def generated_file_name():
    yield File(
        name=f'test_file_{fake_en.name()}_{random.randint(0, 10)}'
    )


def generated_file():
    path = rf"{os.path.split(os.environ['VIRTUAL_ENV'])[0]}\data\test_file_{random.randint(0, 999)}.txt"
    text = f'Hello World{random.randint(0, 999)}'
    file = open(path, 'w+')
    file.write(text)
    file.close()
    return file.name, path, text
