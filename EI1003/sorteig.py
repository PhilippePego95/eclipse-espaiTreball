import random

print("-------------Sorteig---------------\n")
candidats=int(input("Disme el numero de candidats: "))
guanyadors=int(input("Disme el numero de guanyadors: "))
print("")
llista=[]
if candidats>guanyadors:
    for i in range(candidats):
        nom=input("Candidat {0}: ".format(i+1))
        llista.append(nom)
    print("")  
    print("..............Guanyadors.................")
    for j in range(guanyadors):
        aleatori=random.randint(0,guanyadors-j)
        print("{0} - Guanyador: {1}".format(1+j,llista[aleatori]))
        del llista[aleatori]
else: 
    print("Tots guanyen!!")