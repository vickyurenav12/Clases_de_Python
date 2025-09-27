"""

def saludos(idioma):
    if idioma == "esp":
        print("hola")
    elif idioma == "ale": 
        print("guten Tag")
    elif idioma == "ita": 
        print("ciao")
    else: 
        print ("hello")

i = input("ingresa saludo(esp,ale,ita,eng): ")
saludos(i)

#parametro = idioma 
#argumento = i 

#funcion termina en RETURN 

"""
#para poder ver el resukltado de return, guardar la info en una variable (final)
def saludos(idioma):
    if idioma == "esp":
        return "hola"
    elif idioma == "ale": 
        return "guten Tag"
    elif idioma == "ita": 
        return "ciao"
    else: 
        return "hello"

n= input("ingresa tu nombre: ")
i = input("ingresa saludo(esp,ale,ita,eng): ")
final= saludos(i)
print(final,n)
