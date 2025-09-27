
# para hacer comments y no tome en cuanta el codigo: """" 
"""
def write():
    print('hoy')
    print('hoy es 12')
    print('chao')
write()
write ()
write()
write()

#regla de tres: sacar nota a base de 25%
porcentaje_total= 25 
x =float(input('insertar nota:'))
resultado = (x*100)/(25)24
print(resultado)
"""

"""
#regla de tres: sacar nota a base de 25% pero con FUNCION
#print: muestra valor al usuario
def calcular_nota(porcentaje_total): 
    x =float(input('insertar nota:'))
    resultado = (x*100)/(porcentaje_total)
    print(resultado)
    
   
   
porcentaje=float(input('ingresa el porcentaje total del examen'))  
calcular_nota(porcentaje) 

porcentaje2=float(input('ingresa el porcentaje total del examen'))  
calcular_nota(porcentaje2) 

""" 
#lo mismo pero con return 
#return= guardar info 
def calcular_nota_return(porcentaje_total): 
    x =float(input('insertar nota:'))
    resultado = (x*100)/(porcentaje_total)
    return resultado
    
porcentaje3=float(input('ingresa el porcentaje total del examen'))  
result = calcular_nota_return(porcentaje3)
print(result)