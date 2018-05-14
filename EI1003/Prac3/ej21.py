#autor Philippe Gonzalez Miralles                      {8 Novembre 2017}                                  UJI

def es_letra_castellana(caracter):
    
    alfabeto="áéíóúüabcdefghijklmnñopqrstuvwxyz"

    return caracter.lower() in alfabeto


     
    
def primer_no_castellano(cadena):
   
        
    #cadena=cadena.lower()        
    for caracter in cadena:        
        
        if not es_letra_castellana(caracter):               
            return caracter
    
    return None        
   

print("Ve introduciendo palabras, o vacío para acabar...")

cadena=input("Nueva palabra: ")

while len(cadena)>0:
        

    if  primer_no_castellano(cadena)==None:
        print("Podría ser una palabra correcta")
    else:
        print("Contiene un carácter que no es del alfabeto castellano: '{0}'".format(primer_no_castellano(cadena)))
    

    cadena=input("Nueva palabra: ")
        


print("¡Adiós!")





