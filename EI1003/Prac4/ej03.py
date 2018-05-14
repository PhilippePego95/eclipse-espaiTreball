#autor: Philippe Gonzalez Miralles                        [16 Novembre]                            UJI

print("Ve introduciendo números enteros positivos, o un número negativo para acabar...")

num=int(input("Nuevo número: "))
pares=[]
impares=[]
while num>=0:
    if num%2==0:
        
        pares.append(num)
    else:
        impares.append(num)
    num=int(input("Nuevo número: "))


print("Números pares: {0}".format(pares))
print("Números impares: {0}".format(impares))