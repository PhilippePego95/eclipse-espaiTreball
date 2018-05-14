cant=int(input("Introduce la cantidad de kWh: "))
if cant <=100:
    opc=cant*0.05
    
elif cant <=250:
    sum1=100*0.05
    sum2 =(cant-100) *0.07
    opc = sum1+sum2
    

else:
    opc1=100*0.05    
    opc2=150*0.07    
    opc3=(cant-250)*0.10
    
    opc=opc1+opc2+opc3
    
    
print("Importe: {0:.2f} euros".format(opc))
    