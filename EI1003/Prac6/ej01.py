#autor: Philippe Gonzalez Miralles                        [18 Desembre]                            UJI

nombre_fichero = input('Introduce el nombre de un fichero: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura
alfabet="abcdefghijklmnopqrstuvwxyz"
numero=0
letra=0
for linea in fichero:
    
    for i in range(len(linea)):
        if linea[i].isdigit():
            numero+=1
        elif linea[i].lower()  in alfabet:
            letra+=1
        
    
fichero.close() # Cerrar el fichero
print("Dígitos decimales:",numero)
print("Letras del inglés:",letra)