print ("=============================")
print ("Registrate en esta plataforma")
print ("============================= \n")
nombre = input ("Bienvenido(a), Cual es tu nombre?: ")
print ("Nos da gusto conocerte " + nombre + " vamos a empezar con tu registro: \n")
edad = int (input ("Cual es tu edad?: "))
nombreUsuario = input ("Introduce un nombre de usuario: ")
contraseña = input ("Crea una contraseña (puede contener letras y numeros): ")
if nombreUsuario == contraseña:
    print ("Usuario y contraseña no pueden ser iguales")
    elif edad == 18 or edad > 18:
    opcion_1 = input ("\n Tu cuenta sera para adultos o empresarial?: ")
    opcion_1 = opcion_1.lower()
    if opcion_1 == 'adultos':
        print (nombre + " su cuenta sera creada para adultos.")
    elif opcion_1 == 'empresarial':
         print (nombre + " su cuenta sera creada para una empresa.")
    else:
         print ("Esta opcion no existe")

elif edad >= 13 :
    print ("Tu cuenta ha sido creada para adolescentes.")
elif edad >=7:
    print ("Tu cuenta ha sido creada para menores.")
elif edad <7:
    print ("No cumples con la edad minima.")
elif not nombreUsuario == contraseña:
    print (nombreUsuario + " tu cuenta ha sido creada.")
else:
   print ("No cumples con alguno de los requisitos.")
