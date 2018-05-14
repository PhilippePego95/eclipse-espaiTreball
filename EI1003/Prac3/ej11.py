#autor Philippe Gonzalez Miralles                      (2 Novembre 2017)                                  UJI

def contar_divisores(enter):
    num=enter
    cont=0
    for i in range (1,enter+1,1):
        if num%i==0:
            cont=cont+1
    return cont
def es_primo(num):
    return contar_divisores(num)==2

num=int(input("Introduce un entero estrictamente positivo: "))
num2=int(input("Introduce un entero mayor que {0}: ".format(num)))

print("Voy a buscar primos entre {0} y {1}...".format(num,num2))
print("Encontrados: ",end="")
var =0
for i in range (num,num2+1):
    
    if es_primo(i):
        print(i,end=" ")
        var=i
if var==0:
    print("ninguno")