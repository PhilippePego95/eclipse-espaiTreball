from math import sin
def área_triangulo(l1,l2,a):
    return (l1*l2*sin(a))/2

lado1=float(input("Introduce el primer lado: "))
lado2=float(input("Introduce el segundo lado: "))
angulo=float(input("Introduce el ángulo (en radianes): "))

print("El área del triángulo es: ",área_triangulo(lado1,lado2,angulo))
