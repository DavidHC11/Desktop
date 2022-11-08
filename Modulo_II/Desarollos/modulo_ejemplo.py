from random import randint, seed

print("Hola soy tu primer modulo")


def suma_lista(lista):
    suma = 0
    for x in lista:
        suma = suma + x

    return suma

def lista_alea(n):
    return [randint(1,1000) for x in range(n)]
