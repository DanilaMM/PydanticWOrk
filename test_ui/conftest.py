# конфтест только для ui
import pytest


@pytest.fixture
def ui_fixture():
    return 'Фикстура для ui тестов'
