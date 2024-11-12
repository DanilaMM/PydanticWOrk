# конфтест для всех нагруз тестов
import pytest


@pytest.fixture
def nagruz_fixture():
    return 'Фикстура для нагрузочных тестов'
