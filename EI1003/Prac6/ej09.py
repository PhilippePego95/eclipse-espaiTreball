#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

def todos_dígitos(cad):
    for i in cad:
        if not i.isdigit():
            return False
    return True
#*************************************
nombre_fichero = input('Introduce el nombre de un fichero: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura

for linea in fichero:     
    cadena=linea.rstrip().split()
    for palabra in cadena:
        if todos_dígitos(palabra):
            print(palabra)
        
    
fichero.close() # Cerrar el fichero7634552U#*bcadba*aa
