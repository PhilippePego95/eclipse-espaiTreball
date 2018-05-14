#autor Philippe Gonzalez Miralles                      {7 Novembre 2017}                                  UJI

def abc(palabra):
    alfabeto="áéíóúüabcdefghijklmnñopqrstuvwxyz"
    a=""
    
    palabra=palabra.lower()
    opc=True
    for i in palabra:
        
        if opc==True:
            opc=False
            
            for j in alfabeto:
              
                if i==j:
                    
                    opc=True
              
            if opc==False:
               
                a+=i
    if opc==False:
        print("Contiene un carácter que no es del alfabeto castellano: '{0}'".format(a[0]))
        
    else:
        print("Podría ser una palabra correcta")
        
        
print("Ve introduciendo palabras, o vacío para acabar...")
cadena=input("Nueva palabra: ")

while len(cadena)>0:
    
    abc(cadena)
    
    cadena=input("Nueva palabra: ")
    
print("¡Adiós!")





