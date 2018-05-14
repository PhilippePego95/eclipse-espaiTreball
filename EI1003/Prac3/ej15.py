#autor Philippe Gonzalez Miralles                      {6 Novembre 2017}                                  UJI

nA=int(input("Introduce A: "))
nB=int(input("Introduce B: "))

C=("{0}{1}".format(nA,nB))
R=C*nB
R1=int(R)
S=R1+nA
print("C, concatenación de A y B:",C)
print("R, repetición de C un número B de veces:",R)
print("S, suma de los números representados por R y A:",S)
