from math import sqrt
A=int(input("Introduce a: "))
B=int(input("Introduce b: "))
C=int(input("Introduce c: "))

opc1=(-B+sqrt((B**2)-4*A*C))/(2*A)
opc2=(-B-sqrt((B**2)-4*A*C))/(2*A)

print("x1 = ",opc1)
print("x2 = ",opc2)