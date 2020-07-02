# Para tributar un determinado impuesto se debe ser mayor de 16 años y
# tener unos ingresos iguales o superiores a 1000 € mensuales
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales
# muestre por pantalla si el usuario tiene que tributar o no

# codigo
edad = int(input('Ingrese su edad:'))
ingre = float(input('ingrese su ingreso mensual:'))
if edad > 16 and ingre >= 1000:
    print('Usted debe pagar impuestos !')
else:
    print('Usted no debe pagar impuestos !')
