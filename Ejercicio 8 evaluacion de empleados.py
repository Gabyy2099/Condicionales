# En una determinada empresa, sus empleados son evaluados al final de cada año
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más
# pero no valores intermedios entre las cifras mencionadas
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento
# así como la cantidad de dinero que recibirá el usuario.

# Codigo:

# Tabla de valores:
print('-' * 42)
print('|''{:<29}'.format('Nivel'), '{:<5}'.format('Puntuacion') + str('|'))
print('-' * 42)
print('|''{:<30}'.format('Inaceptable'), '{:<9}'.format('0,0') + str('|'))
print('|''{:<30}'.format('Aceptable'), '{:<9}'.format('0,4') + str('|'))
print('|''{:<30}'.format('Meritorio'), '{:<5}'.format('0,6 o mas') + str('|'))
print('-' * 42, '\n')

# Lectura de puntuacion y muestra de dinero correspodiente:
dinero = 2400
puntos = float(input('Ingrese la puntuacion obtenida:'))
if puntos == 0.0:
    print('Su Nivel de rendimiento fue Inaceptable y su dinero correspodiente es', '$' + str(dinero * puntos))
elif puntos == 0.4:
    print('Su Nivel de rendimiento fue aceptable y su dinero correspidiente es', '$' + str(dinero * puntos))
elif puntos >= 0.6:
    print('Su Nivel de rendimiento fue meritorio y su dinero correspondiente es', '$' + str(dinero * puntos))
else:
    print('La cantidad de puntos ingresada no es correcta')
