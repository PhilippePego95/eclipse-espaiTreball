import math
veces=int(input("¿Cuántas veces prevés utilizar el gimnasio? "))
#tarjeta 50
#bono personal 10 sesiones 20
#entrada 3
bonos= math.ceil(veces/10)
opcB= bonos*20


bono= veces//10
entrada= veces%10
opcBE=bono*20+entrada*3

preu=50
oferta="tarjeta."
if preu>opcB:
    preu=opcB
    oferta="bonos."
if preu>opcBE:
    preu=opcBE
    oferta="bonos y entradas."
   
print("Con tarjeta: 50 euros.")
print("Con bonos ({0}): {1} euros.".format(bonos,opcB))
print("Con bonos ({0}) y entradas ({1}): {2} euros.".format(bono,entrada,opcBE))
print("Recomendación: {0}".format(oferta))




