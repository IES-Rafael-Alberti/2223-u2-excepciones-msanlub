from src.ejercicio4 import entrada
import pytest

def test_noEsNumero():
    with pytest.raises(TypeError):
        entrada("hola")