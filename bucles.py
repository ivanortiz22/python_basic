

def run():
    contador = 0
    LIMITE=1000000
    potencia = 2**contador
    while potencia < LIMITE:
        print("2 elvavado a "+str(contador)+"es igual a" +str(potencia))
        contador= contador+1
        potencia= 2**contador



if __name__ == '__main__':
    run()


