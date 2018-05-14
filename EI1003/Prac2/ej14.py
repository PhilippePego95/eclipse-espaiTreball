preu=float(input("Introduce el importe de la compra: "))
zona = input("Introduce la zona de envío (A/B/C): ")
soci = input("¿Eres socio (S/N)? ")

def compra(preus):

    if preus<=150:
        if soci == "S" or soci =="s":
            a=19
        else:
            a=25
    elif preus<=750:
        if soci == "S" or soci =="s":
            a=49
        else:
            a=60
    elif preus<=1500:
        if soci == "S" or soci =="s":
            a=89
        else:
            a=120   
    else:
        if soci == "S" or soci =="s":
            a= preus*0.06
        else:
            a=preus*0.08
    return a;


if zona == "A" or zona =="a":
    gastos=(compra(preu))
elif zona =="B" or zona =="b":
    gastos=(compra(preu)+30)
elif zona =="C" or zona =="c" :
    gastos=(compra(preu)+69)
else:
    gastos=(0)


print("Gastos de envío: {0:.2f} euros".format(gastos))


    
    