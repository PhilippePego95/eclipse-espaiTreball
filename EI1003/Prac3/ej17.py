#autor Philippe Gonzalez Miralles                      {7 Novembre 2017}                                  UJI

def todos_dígitos(cad):
    tot=True
    for i in cad:
        if i.isdigit()==False:
            tot=False
    return tot

cad=input("Introduce una cadena de caracteres: ")
var=todos_dígitos(cad)
if var!=True:
    print("No todos los caracteres son dígitos")
else:
    print("Todos los caracteres son dígitos")