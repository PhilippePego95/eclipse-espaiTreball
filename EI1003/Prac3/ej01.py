#autor Philippe Gonzalez Miralles

from math import pi
def área_círculo(radio):
    return pi * radio ** 2

def longitud_circunferencia(radio):
    return pi * radio * 2

rad=float(input("Introduce el radio: "))
print("Área: {0:.2f}".format(área_círculo(rad)))
print("Longitud: {0:.2f}".format(longitud_circunferencia(rad)))