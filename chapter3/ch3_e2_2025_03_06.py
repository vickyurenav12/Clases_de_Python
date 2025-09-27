try:
    #le pedimos al usuario que ingresa horas y rate 
    hours = float(input('ingresa horas de trabajo:'))
    rate = float(input('ingresa pago por hora:'))

    if hours >40:
        add= rate*(hours-40)*1.5 
        #calculamos pay
        pay=(40*rate)+add 
    else:
        pay= hours*rate

    #imprimimos el pago
    print('el pago por hora es',pay)
except: 
    print('Error,pleacse enter numeric input')
 