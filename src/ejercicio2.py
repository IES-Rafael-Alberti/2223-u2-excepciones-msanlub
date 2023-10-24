#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numeroImpar(numero:int) -> int:
    '''función que da la serie de numero impares'''
    impares = []
    for impar in range(numero):
        if impar % 2 != 0:
            impares.append(impar)
    return impares

if __name__=="__main__":
    try:
        #entrada
        numero = int(input("Escribe un numero: "))
        #proceso
        impar = numeroImpar(numero)
        #salida
        for valor in impar:
            print(valor)
    except ValueError:
        raise ValueError("Debe ingresar un número.")
        