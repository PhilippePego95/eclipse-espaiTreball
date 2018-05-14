triangulo=True

while triangulo==True:
    a=int(input("Introduce el lado a: "))
    b=int(input("Introduce el lado b: "))
    c=int(input("Introduce el lado c: "))
    if a+b>c and c+b>a:
        if a==b==c:
            print("Es equilátero")
        elif a==b or b==c or a==c:
            print("Es isósceles")
        elif a!=b and a!=c and b!=c:
            print("Es escaleno")
        triangulo=False
   
    else:
        print("No es un triángulo\n")