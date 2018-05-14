from math import pi,sin
def área_triangulo(l1,l2,a):
    a=(a*pi)/180
    return (l1*l2*sin(a))/2

lado1=float(input("Introduce el primer lado: "))
lado2=float(input("Introduce el segundo lado: "))
angulo=float(input("Introduce el ángulo (en grados): "))

print("El área del triángulo es: ",área_triangulo(lado1,lado2,angulo))
