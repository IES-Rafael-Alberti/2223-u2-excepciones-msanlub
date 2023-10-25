#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!" 

CONTRASEÑA = "123456"

def checkPassword(passw,CONTRASEÑA):
    '''función que repite hasta tener la contraseña correcta'''
    return passw == CONTRASEÑA

if __name__=="__main__":
    passwordOk = False
    while not passwordOk: 
        try:
            #entrada
            passw = input("Introduce la contraseña correcta:\n")
            #proceso
            passwordOk = checkPassword(passw,CONTRASEÑA)
            raise NameError('Incorrect')
        except NameError: #Si no es la contraseña correcta
            print('Incorrent Password!!!')
    #salida
    print("Contraseña correcta.")