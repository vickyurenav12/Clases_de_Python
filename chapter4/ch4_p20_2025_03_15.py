
"""
def addnum(a,b,c,d,e): 
    add= a + b - c/d * e
    return add

x=addnum(4,9,7,6,100)
print(x)
"""

#funcion para sacra el 7%
def calc(precio): 
    x= precio*0.07
    return x

precio= float(input("ingresa precio del producto: "))
porciento = calc(precio)
total = precio + porciento
print("el 7 porciento de la compra es:", porciento)
print("el total de la compra es: ", total)
    