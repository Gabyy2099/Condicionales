# Escribir un programa que solicite al usuario un numero
# mostrar por pantalla si es par o impar

# Codigo:
num = float(input('Ingrese un numero :'))
resto = num % 2
if resto == 0:
    print('El numero ingresado es par.')
else:
    print('El numero ingresado es impar.')
