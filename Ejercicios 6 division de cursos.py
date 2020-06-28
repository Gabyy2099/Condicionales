# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
# el grupo B por el resto
# Escribir un programa que pregunte al usuario su nombre y sexo y mostrar por pantalla su grupo correspondiente

# codigo:
genero = input('Ingrese su genero:')
nom = input('Ingrese su nombre:')
if (genero.lower() == 'mujer' and nom.lower() < 'm') or (genero.lower() == 'hombre' and nom.lower() > 'n'):
    print('Usted pertenece al grupo A !')
else:
    print('Usted pertenece al grupo B !')
