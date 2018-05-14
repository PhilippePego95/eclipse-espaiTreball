#autor: Philippe Gonzalez Miralles                        [22 Novembre]                            UJI

def candidatura():
    candidat=input("Nueva candidatura: ")
    candidats=[]
    while len(candidat)>0:
        candidats.append(candidat)
        candidat=input("Nueva candidatura: ")
    return candidats

def votos(lista):
    vots=[]
    for i in range (len(lista)):
        voto= input("Votos para {0}: ".format(lista[i]))
        vots.append(voto)
    return vots
def media(candidats,vots):
    suma=0
    for i in range (len(vots)):
        suma+=int(vots[i])
    
    for i in range (len(vots)):
        media= (int(vots[i])*100)/suma
        print(" {0:.2f}% de los votos a candidaturas para {1}".format(media,candidats[i]))
#********************************************   

print("Ve introduciendo candidaturas, o vacío para acabar...")

candidats=candidatura()
vots=votos(candidats)
media(candidats, vots)


