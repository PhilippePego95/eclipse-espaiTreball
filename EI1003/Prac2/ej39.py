sp=" "
a=int(input("Introduce un número entero: "))
b=2
def primo(n):
    a=0
    for i in range(1,n+1):
        if(n % i==0):
            a=a+1
    if(a==2):
        return(i)
    
    
    
cadena=""
for j in range (1,a,1):
    num=primo(j)
    if num!=None:
        cadena=cadena+sp+str(num)
#print(cadena)

print("Los números primos menores que {0} son:{1}".format(a,cadena))


#print("Los números primos meninores que {0} son: {1}".format(a,cad))



