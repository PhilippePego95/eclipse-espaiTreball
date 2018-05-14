#autor: Philippe Gonzalez Miralles                        [23 Novembre]                            UJI

from moduloimagen import leerImagen, mostrarImagen

nombreFichero = input("Introduce el nombre de la imagen: ")

matriz = leerImagen(nombreFichero)

mostrarImagen(matriz)
