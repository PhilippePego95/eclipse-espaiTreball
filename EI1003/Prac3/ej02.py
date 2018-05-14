#autor Philippe Gonzalez Miralles

def es_triángulo(a,b,c):
    return (a+b>c and c+b>a and c+a>b)


a=float(input("Introduce el número a: "))
b=float(input("Introduce el número b: "))
c=float(input("Introduce el número c: "))

if es_triángulo(a, b, c)==True:
    print("Es un triángulo")
else:
    print("No es un triángulo")


