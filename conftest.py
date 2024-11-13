#Конфтест для всех тестов, и ui и api

import pytest


@pytest.fixture
def alltest_fixture():
    return 'Фикстура для всех тестов'