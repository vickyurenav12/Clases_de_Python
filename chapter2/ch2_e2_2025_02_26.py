#le pedimos al usuario que ingresa horas y rate 
hours = float(input('ingresa horas de trabajo:'))
rate = float(input('ingresa pago por hora:'))

#calculamos pay
pay=hours*rate

#imprimimos el pago
print('el pago por hora es',pay)