#autor Philippe Gonzalez Miralles                      {25 Novembre 2017}                                  UJI



def eliminar(cad):
    if len(cad)>0:
        neta=False
        netF=False
        #primera part
        i=0
        while neta==False:
            if cad[0]==" "or cad[0]=="-":
               
                    cad=cad[1:]
                    i+=1
                
            else:
                         
                neta=True
                
            if len(cad)==2:
                neta=True
                
                
        #segona part      
        final=len(cad)-1  
             
        while netF==False:
            if cad[final]==" "or cad[final]=="-" and final!=0:
                cad=cad[:final]
                final-=1
            
            else:
                     
                netF=True
        
        if cad[0]=="-":
            cad=""      
        
    return cad
                
cadena=input("Introduce una cadena de caracteres: ")

nova=(eliminar(cadena))
        
        
print("Cadena limpiada: =>{0}<=".format(nova))
print("Cadena original: =>{0}<=".format(cadena))





