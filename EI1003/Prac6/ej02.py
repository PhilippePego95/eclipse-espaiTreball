#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

nombre_fichero = input('Introduce el nombre de un fichero de test: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura

plantilla=fichero.readline()

for linea in fichero:    
    cadena=linea.split("#")
    if len(cadena)>1:
        print("El alumno con DNI {0} ha respondido {1}".format(cadena[0],cadena[1]))

        
    
fichero.close() # Cerrar el fichero
print("Un alumno perfecto habría respondido",plantilla)