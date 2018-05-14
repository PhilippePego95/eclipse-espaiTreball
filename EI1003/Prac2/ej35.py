num=int(input("Introduce un número entero: "))

a=1
factorial=1

while factorial <=num:  
      
    factorial=factorial*a
    
    if factorial<=num:
        menor=a
    if factorial>num:        
        major=a
    a=a+1
    #print("{0}! = {1}".format(numero,factorial))
print("El número buscado es {0} ({1}! <= {2} < {0}!)".format(major,menor,num))
