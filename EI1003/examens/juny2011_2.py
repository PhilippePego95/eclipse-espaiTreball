class Equipos:
    def __init__(self,nom,gols,golsEn,punts):
        self.nom=nom
        self.gols=gols
        self.golsEn=golsEn
        self.punts=punts
    def actualizar(self,gols,golsEn,punts):
        
        self.gols+=gols
        self.golsEn+=golsEn
        self.punts+=punts

#**************************************************
def crearListaEquipos(fitxer):
    fichero=open(fitxer,"r")
    lista=[]
    l=[]
    primer=True
    for linia in fichero:
        datos =linia.rstrip().split("#")
        
        gol=int(datos[1])
        golE=int(datos[3])
        resta= gol-golE
        if resta>0:
            puntsLocal=3
            puntsVis=0

        elif resta<0:
            puntsVis=3
            puntsLocal=0

        else:
            puntsLocal=1
            puntsVis=1
                    
        if primer:
            partit=Equipos(datos[0],gol,golE,puntsLocal)
            partit2=Equipos(datos[2],golE,gol,puntsVis)
            lista.append(partit)
            lista.append(partit2)
            l.append(datos[0])
            l.append(datos[2])

            primer =False
        else:
            for i in range(len(lista)):

                if not datos[0] in l:
                    partit=Equipos(datos[0],gol,golE,puntsLocal)
                    lista.append(partit)
                    l.append(datos[0])
                    break
                elif lista[i].nom==datos[0]:
                    lista[i].actualizar(gol,golE,puntsLocal)
                    break
           
            for i in range(len(lista)):
   
                if not datos[2] in l:
                    partit2=Equipos(datos[2],golE,gol,puntsVis)
                    lista.append(partit2)
                    l.append(datos[2])
                    break

                elif lista[i].nom==datos[2]:
                    lista[i].actualizar(golE,gol,puntsVis)
                    break
                                    
    fichero.close()      
    return lista

def obtenerGanador(lista):
    ganador=lista[0].nom
    maxi=lista[0].punts
    dif=lista[0].gols - lista[0].golsEn
    for i in range(len(lista)):
        if lista[i].punts>maxi:
            ganador=lista[i].nom
            maxi=lista[i].punts
            dif=lista[i].gols - lista[i].golsEn
        elif lista[i].punts>=maxi:
                diff=lista[i].gols - lista[i].golsEn
                if diff>dif:
                    ganador=lista[i].nom
                    maxi=lista[i].punts
                    dif=lista[i].gols - lista[i].golsEn
    return ganador 
            
def equiposGoleados(fitxer):
    fichero=open(fitxer,"r")
    goleada=[]
    for linia in fichero:
        datos=linia.rstrip().split("#")
        local=datos[0]
        visitant=datos[2]
        gol=int(datos[1])
        golEn=int(datos[3])
        resta= gol-golEn
        
        if resta>=4 and not visitant in goleada:
            goleada.append(visitant)
        if resta<=-4 and not local in goleada:
            goleada.append(local)
                  
    fichero.close()
    return goleada    
    
    
lista=crearListaEquipos("partits.txt")  
print("----------------------------------")
print("                         Gols")
print("               -------------------")

print("Equip\tPunts\tA favor\tEn contra")
print("----------------------------------")

for i in range(len(lista)):

        print("{0}\t{3}\t{1}\t{2}".format(lista[i].nom,lista[i].gols,lista[i].golsEn,lista[i].punts))

ganador=obtenerGanador(lista)   
goleada=equiposGoleados("partits.txt")
print("----------------------------------")

print("El equip guanyador és",ganador) 
print("-----------------------------------")    
print("Els equips golejats son:",goleada)
print("-----------------------------------")    


            
            
            
    