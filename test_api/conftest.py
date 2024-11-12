#конфтест для всех api тестов, и нагруз и функциональных

import pytest


@pytest.fixture
def allapi_fixture():
    return 'Фикстура для всех api тестов'