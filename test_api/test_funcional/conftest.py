# конфтест для функциональных
import pytest


@pytest.fixture
def allapi_fixture():
    return 'Переопределенная фикстура для функиональных тестов'
