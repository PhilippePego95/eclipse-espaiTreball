#autor Philippe Gonzalez Miralles                      {6 Novembre 2017}                                  UJI

def todos_dígitos(cad):
    tot=True
    num=0
    suma=0
    digit=""
    dig=False
    pos=0
    for i in cad:
        if i.isdigit()==False:
            tot=False
            if dig!=True:
                digit=i
                pos=num
                dig=True
        if tot==True:
            num+=1
            suma+=int(i)
    if tot==True:
        print("Todos los caracteres son dígitos")
        print("¿Cuántos dígitos?",num)
        print("¿Suma de dígitos?",suma)
    else:
        print("Primer \"no dígito\": '{0}' en posición {1}".format(digit,pos))
    return tot

cad=input("Introduce una cadena de caracteres: ")
var=todos_dígitos(cad)
