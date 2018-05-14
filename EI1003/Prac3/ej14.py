#autor Philippe Gonzalez Miralles                      {2 Novembre 2017}                                  UJI

cadena=input("Introduce un texto (vacío para acabar): ")

tot=len(cadena)

maxi=cadena        
maxNum=tot
minCad=cadena
minNum=tot

if tot>0:
#************PROGRMA***********
    while tot>0:
        
        tot= len(cadena)
        
        if tot>0:
            if tot >= maxNum:
                maxNum=tot
                maxi=cadena
            if tot <= minNum:
                minNum=tot
                minCad=cadena   
            cadena=input("Introduce otro texto (vacío para acabar): ")
         
            
            
    print("Última cadena de mínima longitud, {0}: =>{1}<=".format(minNum,minCad))
    print("Última cadena de máxima longitud, {0}: =>{1}<=".format(maxNum,maxi))
else: 
    print("No se ha introducido ningún texto")