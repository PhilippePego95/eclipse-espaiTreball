#autor: Philippe Gonzalez Miralles                        [11 Desembre]                            UJI

def repeticiones(lista):
    rep=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i!=j:
                if lista[i]==lista[j] and not i in rep:#comprovem que no fiquem la mateixa posició mes d'una vegada
                    rep.append(i)                       #amb un breaktambe serviria
    #print(rep) #amb el print podem comprobar que la llista torna ordenada
    return rep

def eliminar(matriu):
    for i in range(len(matriu)):
        lista=repeticiones(matriu[i])
        for j in lista:
            matriu[i][j]=0
#*****************************************
#Exemple del programa principal

print("Examen Programació I\t[11 de Desembre]\tUJI")
print("------------------------------------------------------")
                    #  -MATRIU-
                    #[1,2,3,3,7]
                    #[3,5,3,1,1]
                    #[4,5,6,4,2]
matriu=[[1,2,3,3,3,7],[3,5,3,1,1],[2,4,5,6,4]]  
print("Matriu original:")
print(matriu)
eliminar(matriu)
print("------------------------------------------------------")

print("Matriu modificada:")
print(matriu)
print("------------------------------------------------------")



