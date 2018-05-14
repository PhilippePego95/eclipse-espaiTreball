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
cont=1
total=0
while total<num:     
#for j in range(1,num,1):

    if abundant(cont) ==True:
        cadena=cadena+str(cont)+sp
        total=total+1
    cont=cont+1
        #print(j)
        
print("Los {0} primeros números abundantes son: {1}".format(num,cadena))