pesos= input("cuantos pesos colombianos tienes ?:  ")
pesos =float(pesos)
valor_dolar = 3875
dolares= pesos/valor_dolar
dolares = round(dolares,2)

resultado = str(dolares)

print ("tienes $"+resultado+"dolares")