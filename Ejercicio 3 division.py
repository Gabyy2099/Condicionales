# Escribir un programa que pida al usuario dos numeros y muestre por pantalla su division
# si el divisor es 0 (cero) mostrar un error !

# codigo:
num_1 = float(input('Ingrese el dividendo :'))
num_2 = float(input('Ingrese el divisor :'))
if num_2 != 0:
    print('La division entre ', num_1, ' y ', num_2, ' Es ', round(num_1 / num_2, 2))
else:
    print('Error !!!!! el divisor no puede ser 0')
