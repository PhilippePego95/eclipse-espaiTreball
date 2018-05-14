fib=int(input("Introduce un número entero: "))
opc=1
opc2=0
num=1
for i in range (1,fib,1):
    aux=opc+opc2
    opc=opc2
    opc2=aux
    num=opc+opc2
print("Fibonacci({0}) = {1}".format(fib,num))
    