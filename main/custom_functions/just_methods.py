"""
Los comentarios está ocultos para ver más fácil el código, al hacer clic en "+" en la parte
izquierda del editor (yo estoy trabajando con PyCharm para este laboratorio (en la linea 10 por ejemplo)
"""


def calcular_promedio(lista):

    suma = 0
    cont = len(lista)

    '''
    Recorro la lista sacando cada uno de los elementos
    y guardando momentaneamente cada uno en la variable "elemento"
    y sumarlo a la suma total
    '''
    for elemento in lista:
        suma += elemento

    '''
    También se pudo hacer de la siguiente manera pero es muy largo:

    recorrrer "i" entre 0 y la longitud de la lista (por ejemplo de 0 a 4
    y luego buscar el elemento en la posición "i" de la lista, de la siguiente manera

    for i in range(0, len(lista)):
        elemento_sum += lista[i]

    Normalmente de una manera similar a esta se hace en java o c, pero Python es nás compacto ;)

    '''

    # La nota final es la suma de todos los elementos dividido en la cantidad de elementos
    # len(lista) es una función que me da la cantidad de elementos en una lista o longitud
    avarage = suma / cont

    return avarage



def calcular_elemento_mayor(lista):

    # Inicialmente, asumamos que la mejor nota es la primera de la lista, es decir la posición 0
    mayor = lista[0]

    '''
    Recorro la lista sacando cada uno de los elementos
    y guardando momentaneamente cada uno en la variable "elemento"
    y sumarlo a la suma total
    '''
    for elemento in lista:
        # Si la nota actual en la que vamos recorriendo la lista es mayor que la mayor
        # entonces la nueva nota mayor será la nota actual
        if elemento > mayor:
            mayor = elemento

    # Al finalizar la nota mayor será la que esté en best_elemento, si ninguna fue mayor que la primera
    # entonces la nota mayor será la primera
    return mayor


def eliminar_menor_elemento(lista):

    # Inicialmente, asumamos que la peor nota es la primera de la lista, es decir la posición 0
    # así que guardo el valor de la nota en la posición 0 e indico que la posición de la peor es 0
    menor_elemento = lista[0]
    posicion_menor_elemento = 0

    # Necesito la cantidad de notas para calcular el promedio
    elementos_cont = len(lista)

    # A la suma final se le debe restar la primera nota
    elemento_suma = 0

    '''
    Recorro la lista sacando cada uno de los elementos
    y guardando momentaneamente cada uno en la variable "elemento"
    '''

    # Antes de iniciar el ciclo llevo un contador de la posición en la que se va
    posicion_cont = 0

    for elemento in lista:
        # Si la nota actual en la que vamos recorriendo la lista es menor que la peor
        # entonces la nueva peor será la nota actual
        # sin embargo debemos recordar que la primera nota fue restada de la suma

        if elemento < menor_elemento:
            # Actualizo la posición de la peor nota y el valor de la peor nota
            posicion_menor_elemento = posicion_cont
            menor_elemento = elemento

        # Una vez finalizado el ciclo, incremento el contador de la posición en 1
        posicion_cont += 1

    # Remuevo la peor nota de la lista, quitando el elemento que está en la posición de la peor nota
    lista.pop(posicion_menor_elemento)

    # Al finalizar se retorna una lista sin la nota menor
    return lista