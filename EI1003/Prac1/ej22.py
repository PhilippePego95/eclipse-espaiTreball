from math import pi
def área_círculo(radio):
    return pi * radio ** 2

def longi_círculo(radio):
    return 2 * pi * radio

rad=float(input("Introduce el radio: "))
print("Área: {0:.2f}".format(área_círculo(rad)))
print("Longitud: {0:.2f} ".format(longi_círculo(rad)))