from math import pi
def área_círculo(radio):
    return pi * radio ** 2

rad=float(input("Introduce el radio: "))
print("Área: ",área_círculo(rad))
