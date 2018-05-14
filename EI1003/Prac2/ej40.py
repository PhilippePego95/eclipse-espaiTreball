
a=int(input("Introduce un número entero: "))
b=2
def primo(n):
    a=0
    for i in range(1,n+1):
        if(n % i==0):
            a=a+1
    if(a==2):
        return(i)
    
    
    
total=1
cont=1
print("Los",a,"primeros números primos son:",end=" ")

#for j in range (1,a,1):
while total<=a:
    num=primo(cont)
    cont=cont+1
    if num!=None:
        total=total+1
        print(num,end=" ")


