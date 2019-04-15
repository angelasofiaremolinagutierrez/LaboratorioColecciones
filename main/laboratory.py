"""
Solución del laboratorio
"""

from custom_functions import just_methods
import math

print("Laboratorio del Observatorio Nacional de Meteorología")
print()

temperaturas = []
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


print("Ingrese las temperaturas de Santander en cada mes del año:")
for x in range(0,12):
    while True:
        try:
            s = float(input(meses[x]+": "))
            temperaturas.append(s)
            break
        except ValueError:
            print("Carácter no válido. Ingreselo otra vez")

santander = temperaturas[0:12]
print("Temperaturas Santander:", santander)

print()
print("Ingrese las temperaturas de Guajira")
for y in range(0,12):
    while True:
        try:
            g = float(input(meses[y]+": "))
            temperaturas.append(g)
            break
        except ValueError:
            print("Carácter no válido. Ingreselo otra vez")

guajira = temperaturas[12:24]
print("Temperaturas Guajira:", guajira)

print()
print("Ingrese las temperaturas de Nariño")
for z in range(0,12):
    while True:
        try:
            n = float(input(meses[z]+": "))
            temperaturas.append(n)
            break
        except ValueError:
            print("Carácter no válido. Ingreselo otra vez")

narino = temperaturas[24:36]
print("Temperaturas Nariño:", narino)


print()
print("A:")

prom_santander = just_methods.calcular_promedio(santander)
prom_guajira = just_methods.calcular_promedio(guajira)
prom_narino = just_methods.calcular_promedio(narino)

print("El promedio de temperatura en Santander es de:", prom_santander, "grados")
print("El promedio de temperatura en la guajira es de:", prom_guajira, "grados")
print("El promedio de temperatura en Nariño es de:", prom_narino, "grados")

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

pos_santander = temperaturas.index(mayor_santander)
pos_guajira = temperaturas.index(mayor_guajira)
pos_narino = temperaturas.index(mayor_narino)
print ("La temperatura más alta en Santander fue de;",mayor_santander,"grados, en el mes de", meses[pos_santander] )
print ("La temperatura más alta en Guajira fue de:",mayor_guajira,"grados, en el mes de", meses[pos_guajira] )
print ("La temperatura más alta en Nariño fue de:",mayor_narino,"grados, en el mes de", meses[pos_narino])

###

print()
print("D:")
mayores = [mayor_santander,mayor_guajira,mayor_narino]
promedio_mayores = just_methods.calcular_promedio(mayores)

print("El promedio de las tres temperaturas más altas es de:", promedio_mayores,"grados")

###

print()
print("E:")
dep_dict = {
    0 : "Santander",
    1 : "La Guajira",
    2 : "Nariño"
}
promedios = [prom_santander,prom_guajira,prom_narino]
mayor_promedio = just_methods.calcular_elemento_mayor(promedios)
pos_promedios = promedios.index(mayor_promedio)

print("El promedio de temperaturas más alto fue el de", dep_dict[pos_promedios],"que fue de: ",mayor_promedio,"grados")

###

print()
print("F:")
mayor_temp = just_methods.calcular_elemento_mayor(mayores)
posicion_mayor = mayores.index(mayor_temp)
posicion_mes = temperaturas.index(mayor_temp)

print("La temperatura más alta fue de", mayor_temp, "grados, en", dep_dict[posicion_mayor],"en el mes de",meses[posicion_mes])

###

print()
print("G:")
de_san = just_methods.calcular_desviacion_estandar(santander)
print("La desviación estandar de la temperatura en Santander es de:" ,de_san,"grados")

de_gua = just_methods.calcular_desviacion_estandar(guajira)
print("La desviación estandar de la temperatura en La Guajira es de:",de_gua,"grados")

de_na = just_methods.calcular_desviacion_estandar(narino)
print("La desviación estandar de la temperatura en Nariño es de:",de_na,"grados")

###

print()

