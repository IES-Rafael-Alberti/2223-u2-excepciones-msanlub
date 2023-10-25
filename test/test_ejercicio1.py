from src.ejercicio1 import repetirEdad
import pytest

def test_EdadNoNumeroError():
    with pytest.raises(TypeError):
        repetirEdad("hola")