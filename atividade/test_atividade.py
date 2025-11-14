import pytest
@pytest.fixture
def lista():
    return [2,3,4,5,6]

def soma_dobro(numeros):
    return sum(x*2 for x in numeros)

def test_soma_dobro(lista):
    assert soma_dobro(lista) == 40