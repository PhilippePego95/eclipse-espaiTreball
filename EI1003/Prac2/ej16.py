numero= int(input("Introduce un número entero: "))
num=1
cadena=""
separador=", "
while num <numero:  
    nums=str(num) 
    cadena=cadena+nums+separador
    num+=1
    
nume=str(numero)
cadena=cadena+nume

print(cadena)