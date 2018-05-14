num=int(input("Introduce un número entero: "))
a=1
for i in range (1,num+1,1):
    a=a*i
    print("{0}! = {1}".format(i,a))
