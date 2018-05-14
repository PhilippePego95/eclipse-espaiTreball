a=float(input("Introduce el lado a: "))
b=float(input("Introduce el lado b: "))
c=float(input("Introduce el lado c: "))

if a**2+b**2==c**2 or c**2+b**2==a**2:
    print("Es rectángulo")
else:
    print("No es rectángulo")