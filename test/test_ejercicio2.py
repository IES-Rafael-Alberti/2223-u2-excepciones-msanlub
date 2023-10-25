from src.ejercicio2 import numeroImpar
import pytest

def test_noEsNumero():
    with pytest.raises(TypeError):
        numeroImpar("hola")