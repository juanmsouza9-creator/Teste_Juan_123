from funcao import*
import pytest
@pytest.fixture
def lista():
    return [2,3,4,5,6]

def test_soma_dobro(lista):
    assert soma_dobro(lista) == 40