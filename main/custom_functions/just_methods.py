import math


def calcular_promedio(lista):

    suma = 0
    cont = len(lista)

    for elemento in lista:
        suma += elemento

    avarage = suma / cont

    return avarage


def calcular_elemento_mayor(lista):

    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento

    return mayor


def calcular_desviacion_estandar(lista):
    # desviación estandar es de=sqrt((sum(x-elem)^2)/n)

    acum = 0
    for x in lista:
        acum = acum + ((abs(x-(calcular_promedio(lista))))**2)

    de = math.sqrt(acum/((len(lista))-1))
    return de

