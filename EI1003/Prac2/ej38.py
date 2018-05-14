fib=int(input("Introduce un número entero: "))
opc=1
opc2=0
num=1
bandera=False

for i in range (0,fib,1):
    aux=opc+opc2
    opc=opc2
    opc2=aux
    num=opc+opc2
    if num ==fib:
        b=i+2
        bandera=True
        
if bandera==True:
    print ("El número buscado es {}".format(b))
else:
    print("No es un número de Fibonacci")
    