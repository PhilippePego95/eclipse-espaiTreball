#autor Philippe Gonzalez Miralles                      {7 Novembre 2017}                                  UJI

cadena=input("Introduce una cadena de dígitos: ")
pos=int(input("Introduce la primera posición que visitar: "))
lon=int(input("Introduce la longitud deseada: "))

for i in range(0,lon):
    a=cadena[pos]
    
    print("Paso {0}: visitada posición {1} con contenido {2}".format(i+1,pos,a))
    pos=int(a)