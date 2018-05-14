#autor Philippe Gonzalez Miralles  (2 Novembre 2017)

def contar_divisores(enter):
    num=enter
    cont=0
    for i in range (1,enter+1,1):
        if num%i==0:
            cont=cont+1
    return cont

#**********************************************
nEnter=int(input("Introduce un número entero: "))
a=0
num=0
for j in range (1,nEnter+1,1):   
    b=contar_divisores(j)
    if a<=b:
        a=b
        num=j

print("El número con más divisores es {0} ({1} divisores)".format(num,a))
    