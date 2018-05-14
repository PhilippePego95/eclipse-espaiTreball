#autor Philippe Gonzalez Miralles                      {6 Novembre 2017}                                  UJI

def provar_cadena(cad):
    tot=False
    for i in cad:
        if i.isdigit()==False:
            tot=True
    return tot

cad=input("Introduce una cadena de caracteres: ")
if provar_cadena(cad)==True:
    print("No todos los caracteres son dígitos")
else:
    print("Todos los caracteres son dígitos")