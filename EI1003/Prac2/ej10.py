num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))


if num1>0 and num2>0 or num1<0 and num2<0:
    print("Su producto es positivo")
elif num1==0 or num2==0:
    print("Su producto es nulo")
elif num1<0 or num2<0:
    print("Su producto es negativo")


