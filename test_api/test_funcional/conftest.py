# конфтест для функциональных
import pytest


@pytest.fixture
def func_fixture():
    return 'Фикстура для функциональных тестов'
