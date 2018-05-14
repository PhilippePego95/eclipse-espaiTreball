#autor Philippe Gonzalez Miralles  -> 30 d'Octubre 2017

def tipo_triángulo(a,b,c):

    if es_triángulo(a,b,c):
        if a==b==c:
            return("equilátero")
        elif a==b or b==c or a==c:
            return("isósceles")
        elif a!=b and a!=c and b!=c:
            return("escaleno")
        else:
            return None
        
def es_triángulo(a,b,c):
    return (a+b>c and c+b>a and c+a>b)

      
triangulo=True

while triangulo==True:
    
    a=int(input("Introduce el lado a: "))
    b=int(input("Introduce el lado b: "))
    c=int(input("Introduce el lado c: "))
    
    tipo=tipo_triángulo(a, b, c)
    if tipo !=None:
        triangulo=False
        
    if tipo == None:  
        print("No es un triángulo\n")
    else:
        print("Es ",tipo)

    
    
    
   
