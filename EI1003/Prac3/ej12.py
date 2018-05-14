#autor Philippe Gonzalez Miralles                      {2 Novembre 2017}                                  UJI

def leer_entero_mayor_que(enter):
    
    num2=int(input("Introduce un entero mayor que {0}: ".format(enter)))
    
    while num2 <= enter:
        num2 = int(input("Esperaba entero mayor que {0} y {1} no lo es. Dame otro: ".format(enter,num2)))

    return num2
        

def contar_divisores(enter):
    num=enter
    cont=0
    for i in range (1,enter+1,1):
        if num%i==0:
            cont=cont+1
    return cont

def es_primo(num):
    return contar_divisores(num)==2

def buscar_primos(num,num2):
    print("Voy a buscar primos entre {0} y {1}...".format(num,num2))
    print("Encontrados: ",end="")
    
    var =0
    for i in range (num,num2+1):
    
        if es_primo(i):
            print(i,end=" ")
            var=i
    if var==0:
        print("ninguno")
        
# Programa ----------------------------------------------


num=leer_entero_mayor_que(0)
num2=leer_entero_mayor_que(num)

buscar_primos(num,num2)
    
    

