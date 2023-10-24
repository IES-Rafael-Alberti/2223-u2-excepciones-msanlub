#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def repetirEdad(edad:int) ->int:
    '''función que repite la edad de entrada de uno en uno'''
    numeros = []
    for numero in range(edad):
        numeros.append(numero+1)
    return numeros

if __name__=="__main__":
    edadCorrecta = False
    edad = None
    while not edadCorrecta:
        try:
            #entrada
            ent = input("Escribe tu edad: ")
            edad = int(ent)
            repetir = repetirEdad(edad)
            edadCorrecta = True
        except ValueError: #si no mete un número
            if edad == None:
                print('Por favor introduzca un número')      
    #salida
    for valor in repetir:
        print(valor)
