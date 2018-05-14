    #Escribe un programa que lea un número entero, n, y escriba el número i cuyo factorial, i!, es n. 
    
    #Supón que el úmero leı́do se corresponde con el factorial de otro número. Un ejemplo de ejecución del programa es:
    
    #Introduce un número entero: 120
    
    #120 es el factorial de 5
    
num=int(input("Introduce un número entero: "))
a=1
i=1
while a<num:
#for i in range (1,num+1,1):
    a=a*i 
   
    if num==a:
       
        print("{0} es el factorial de {1}".format(num,i))
    i=i+1

