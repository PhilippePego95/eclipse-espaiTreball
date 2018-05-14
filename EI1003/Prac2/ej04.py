a=float(input("Introduce el lado a: "))
b=float(input("Introduce el lado b: "))
c=float(input("Introduce el lado c: "))
if a==b==c:
    print("No es isósceles")
elif a==b or b==c or a==c:
    print("Es isósceles")
else:
    print("No es isósceles")