"""
Solución del laboratorio
"""
from custom_functions import just_methods
import math

print("Laboratorio ONM")
print()
#los siguientes son 12 temperaturas registradas por cada
#uno de los tres departamentos durante cada mes del año
print("A:")
temperaturas = [30,28,26,27,24,22,29,28,27,26,28,29,31,33,30,29,29,35,33,31,32,30,28,36,20,18,21,19,13,10,15,11,13,12,14,16]
santander = temperaturas[0:12]
guajira = temperaturas[12:24]
narino = temperaturas[24:36]

prom_santander = just_methods.calcular_promedio(santander)
prom_guajira = just_methods.calcular_promedio(guajira)
prom_narino = just_methods.calcular_promedio(narino)

print ("El promedio de temperatura en Santander es de:",prom_santander,"grados")
print ("El promedio de temperatura en la guajira es de:",prom_guajira,"grados")
print ("El promedio de temperatura en Nariño es de:",prom_narino,"grados")

###

print()
print("B:")
promedio_nacional = just_methods.calcular_promedio(temperaturas)
print("El promedio de temperatura nacional es de:",promedio_nacional,"grados")

###

print()
print("C:")
mayor_santander = just_methods.calcular_elemento_mayor(santander)
mayor_guajira = just_methods.calcular_elemento_mayor(guajira)
mayor_narino = just_methods.calcular_elemento_mayor(narino)

print ("La temperatura más alta en Santander fue de;",mayor_santander,"grados")
print ("La temperatura más alta en Guajira fue de:",mayor_guajira,"grados")
print ("La temperatura más alta en Nariño fue de:",mayor_narino,"grados")

###

print()
print("D:")
mayores = [mayor_santander,mayor_guajira,mayor_narino]
promedio_mayores = just_methods.calcular_promedio(mayores)

print("El promedio de las tres temperaturas más altas es de:",promedio_mayores,"grados")

###

print()
print("E:")
mayor_mayores = just_methods.calcular_elemento_mayor(mayores)

print("El promedio de temperaturas más alto fue de:", mayor_mayores,"grados")

###

print()
print("F:")
mayor_temp = just_methods.calcular_elemento_mayor(mayores)
posicion_mayor = mayores.index(mayor_temp)

dep_dict = {
    0 : "Santander",
    1 : "La Guajira",
    2 : "Nariño"
}

posicion_mes = temperaturas.index(mayor_temp)
meses_dict = {
    0 : "Enero",
    1 : "Febrero",
    2 : "Marzo",
    3 : "Abril",
    4 : "Mayo",
    5 : "Junio",
    6 : "Julio",
    7 : "Agosto",
    8 : "Septiembre",
    9 : "Octubre",
    10 : "Noviembre",
    11 : "Diciembre",

    12 : "Enero",
    13 : "Febrero",
    14 : "Marzo",
    15 : "Abril",
    16 : "Mayo",
    17 : "Junio",
    18 : "Julio",
    19 : "Agosto",
    20 : "Septiembre",
    21 : "Octubre",
    22: "Noviembre",
    23 : "Diciembre",

    24 : "Enero",
    25 : "Febrero",
    26 : "Marzo",
    27 : "Abril",
    28 : "Mayo",
    29 : "Junio",
    30 : "Julio",
    31 : "Agosto",
    32 : "Septiembre",
    33 : "Octubre",
    34 : "Noviembre",
    35 : "Diciembre",

}

print("La temperatura más alta fue de",mayor_temp,"grados, en",dep_dict[posicion_mayor],"en el mes de",meses_dict.get(posicion_mes))

###

print()
print("G:")
#desviación estandar es de=sqrt((sum(x-elem)^2)/n)
acum_sant = 0
for x in santander:
    acum_sant = acum_sant + ((prom_santander-x)**2)

de_sant = math.sqrt(acum_sant/(len(santander)))
print("La desviación estandar de la temperatura en santander es de:" ,de_sant,"grados")

acum_gua = 0
for y in guajira:
    acum_gua = acum_gua + ((prom_guajira-y)**2)

de_gua = math.sqrt(acum_gua/(len(guajira)))
print("La desviación estandar de la temperatura en La Guajira es de:",de_gua,"grados")

acum_na = 0
for z in narino:
    acum_na = acum_na + ((prom_narino-z)**2)

de_na = math.sqrt(acum_na/(len(narino)))
print("La desviación estandar de la temperatura en Nariño es de:",de_na,"grados")

###

print()