
fibonacci="1 "
spa=" "
fib=int(input("Introduce un número entero: "))
opc=1
opc2=0
num=1
for i in range (1,fib,1):
    aux=opc+opc2
    opc=opc2
    opc2=aux
    num=opc+opc2
    fibonacci=fibonacci+str(num)+spa
#print("Fibonacci({0}) = {1}".format(fib,num))
print("Los {0} primeros números de Fibonacci son: {1}".format(fib,fibonacci))
    