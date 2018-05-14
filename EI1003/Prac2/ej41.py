#autor Philippe

def abundant(numero):
    suma=0
    for i in range(1,numero+1,1):
        if numero%i==0:
            suma=suma+i
        #print(i)
    if suma>2*numero:
        return True

num=int(input("Introduce un número entero: "))
cadena=""
sp=" "      
for j in range(1,num,1):
    if abundant(j) ==True:
        cadena=cadena+str(j)+sp
        #print(j)
        
print("Los números abundantes menores que {0} son: {1}".format(num,cadena))