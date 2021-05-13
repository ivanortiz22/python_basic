import random



def run ():
    numero_ale=random.randint(1,100)
    numero_eli= int (input("elige un numero:"))
    while numero_eli != numero_ale:
        if numero_eli< numero_ale:
            print("busca un numero mas grande")
        else:
            print("busca un numero mas pequeno")
        numero_eli= int(input("elige otro numero : "))
    print("ganaste")




if __name__ == '__main__':
    run()