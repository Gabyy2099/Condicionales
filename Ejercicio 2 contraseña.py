# Escribir un programa que almacene en una variable la cadena de caracteres contraseña
# Preguntar al usuario la contraseña y mostrar por pantalla si coincide con la guardada

# Codigo:
contra = 'contraseña'
ingre_contra = input('Ingrese la contraseña:')
if contra == ingre_contra.lower():
    print('Contraseña correcta !!')
else:
    print('Contraseña incorrecta !')
