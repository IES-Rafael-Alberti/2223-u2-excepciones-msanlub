from src.ejercicio5 import checkPassword
import pytest

def test_passwordIncorrecto():
    with pytest.raises(TypeError):
        checkPassword(4303)