#autor Philippe Gonzalez Miralles  (2 Novembre 2017)

def es_abundante(numero):
    suma=0
    for i in range(1,numero+1,1):
        if numero%i==0:
            suma=suma+i
        #print(i)
    return suma>2*numero
        
    
    
    
def sumar_divisores_propios(num):
    i=1
    suma=0
    while i<num:
        if num%i==0:
            suma=suma+i
        i=i+1
    return suma
     


num=int(input("Introduce un número entero: "))
print("Los números abundantes menores que {0} son:".format(num),end=" ")    


suma=0
for j in range(1,num,1):
    if es_abundante(j) ==True:
        
        suma+=j
        print(j,end=" ")
   
    
sumar_divisores_propios(num)