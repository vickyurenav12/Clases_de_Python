"""
print(random.randint(1,100))
"""

import random

print(" ")

num_random= random.randint(1,40)
print('bienvenido al juego de ADIVINA EL NÚMERO, en donde tienes que adivinar el numero en el q estoy pensando entre el 1 y el 40')
print("Escibe un -1 para terminar el juego")
print(" ")

#cant de intentos + 1 // puedo cambiar la cant d intentos sin tener que cambiar nada mas 
n = 11
m = n

while True: 
    n=n-1
    if n == 0:
        print("perdiste, el numero era", num_random)
        break
    
    print('te quedan', n,"intentos")
    try: 
        usuario_guess= int(input('Ingresa el  numero:'))
    except: 
        print("ingresa un número válido")
        print(" ")
        continue
    
    if usuario_guess == -1:
        break
    
    elif usuario_guess == num_random: 
        print('felicidades, lograste completar en',m-n,'intentos!')
        break
    elif usuario_guess > num_random:
        print('numero que estoy pensando es menor que', usuario_guess)
        print(" ")
    else: 
        print('el numero que estoy pensando es mayor a ', usuario_guess )
        print(" ")
    
