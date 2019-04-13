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


def eliminar_menor_elemento(lista):

    menor_elemento = lista[0]
    posicion_menor_elemento = 0

    elementos_cont = len(lista)

    elemento_suma = 0

    posicion_cont = 0

    for elemento in lista:
        if elemento < menor_elemento:
            posicion_menor_elemento = posicion_cont
            menor_elemento = elemento

        posicion_cont += 1

    lista.pop(posicion_menor_elemento)

    return lista


def calcular_desviacion_estandar(lista):
    # desviación estandar es de=sqrt((sum(x-elem)^2)/n)

    acum = 0
    for x in lista:
        acum = acum + ((abs(x-(calcular_promedio(lista))))**2)

    de = math.sqrt(acum/((len(lista))-1))
    return de

