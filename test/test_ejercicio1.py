from src.ejercicio1 import repetirEdad
import pytest

@pytest.mark.parametrize(
    "edad, expected",
    [
        (10,[1,2,3,4,5,6,7,8,9,10]),
        (5,[1,2,3,4,5]),
        (9,[1,2,3,4,5,6,7,8,9])
    ]
)

def test_repetirEdad(edad,expected):
    assert repetirEdad(edad) == expected


def test_repetirEdadError():
    with pytest.raises(ValueError):
        repetirEdad("hola")