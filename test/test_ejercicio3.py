from src.ejercicio3 import listaEntero
import pytest

def test_noEsNumero():
    with pytest.raises(TypeError):
        listaEntero("hola")