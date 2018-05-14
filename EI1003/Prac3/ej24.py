#autor Philippe Gonzalez Miralles                      {8 Novembre 2017}                                  UJI

cadena=input("Introduce una cadena de caracteres A: ")

sufijo=input("Introduce una cadena de caracteres B: ")

if len(cadena)>=len(sufijo):
    es_sufijo = True
    
    for índice in range(len(sufijo)):
    
        if sufijo[-índice-1]!=cadena[-índice-1]:
            
            es_sufijo= False  
            
    if es_sufijo:
        
        print("B es sufijo de A")
    else:
        
        print("B no es sufijo de A")
        
else:
    print("B no es sufijo de A")