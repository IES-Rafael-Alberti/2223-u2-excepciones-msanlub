#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto. 

def listaEntero(entero:int) -> int:
    '''función que da el resultado de la lista desde 0 hasta entero'''
    numeros = []
    for numero in range(entero,-1,-1):
        numeros.append(numero)
    return numeros 

if __name__=="__main__":
    try:
        #entrada
            entero = int(input("Escribe un numero: "))
        #proceso
            lista = listaEntero(entero)
        #salida
            print(lista)
    except ValueError:
        print("Debe ingresar un número.")