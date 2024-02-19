#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def entrada() -> int:
    '''función de entrada que da un entero'''
    numero = int(input("Escribe un número: "))

if __name__=="__main__":
    numero = None
    while numero == None:
        try:
            numero = int(input("Escribe un número: "))
            if numero < 0:
                print("Escribe un número positivo.")
                numero = int(input("Escribe un número: "))
        except ValueError:
            print("Oops!  Eso no es un número entero!")