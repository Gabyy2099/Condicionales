# Escribir un programa que pregunte al usuario su renta anual
# Luego mostrar por pantalla el porcentaje de impuesto correspodiente.

# Codigo:

# Tabla con los montos y porcentajes:
print('Tabla de porcentajes y montos', '\n')
print('-' * 40)
print('|''{:<25}'.format('Montos'), '{:<6}'.format('Porcentajes'), '|')
print('-' * 40)
print('|''{:<30}'.format('Menos de 10000€'), '{:<6}'.format('5%'), '|')
print('|''{:<30}'.format('Entre 10000€ y 20000€'), '{:<6}'.format('15%'), '|')
print('|''{:<30}'.format('Entre 20000€ y 35000€'), '{:<6}'.format('20%'), '|')
print('|''{:<30}'.format('Entre 35000€ y 60000€'), '{:<6}'.format('30%'), '|')
print('|''{:<30}'.format('Mas de 60000€'), '{:<6}'.format('45%'), '|')
print('-'* 40, '\n')

monto = float(input('Ingrese su renta anual:'))
if monto < 10000:
    print('Su porcentaje impositivo es del 5%')
elif monto >= 10000 and monto < 20000:
    print('Su porcentaje impositivo es del 15%')
elif monto >= 20000 and monto < 35000:
    print('Su porcentaje impositivo es del 20%')
elif monto >= 35000 and monto < 60000:
    print('Su porcentaje impositivo es del 30%')
else:
    print('Su porcentaje impositivo es del 45%')
