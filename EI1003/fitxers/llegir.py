nombre_fichero = input('Dame el nombre del fichero: ')
fichero = open(nombre_fichero, 'r') # Abrir en modo lectura
nlinea = 0
for linea in fichero:
    if linea[-1] == '\n':
        linea = linea[:-1]
    nlinea += 1
    print('Linea {0}: |{1}|'.format(nlinea, linea))
fichero.close() # Cerrar el fichero