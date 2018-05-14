#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

nombre_fichero = input('Introduce el nombre de un fichero: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura
tamany=0
cad=""

for linea in fichero: 

              
    cadena=linea.rstrip().split()
    
    for palabra in cadena:
       
        if len(palabra)>tamany:
            tamany=len(palabra)
            cad=palabra
    

        
    
fichero.close() # Cerrar el fichero7634552U#*bcadba*aa


print("Su secuencia de caracteres sin espacios más larga es \"{0}\".".format(cad))