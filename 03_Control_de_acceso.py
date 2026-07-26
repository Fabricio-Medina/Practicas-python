print ("Mini reto.")
nombre = input ("Bienvenido(a), Cual es tu nombre?: ")
print ("Nos da gusto que estes aqui " + nombre + " necesitaremos los siguientes datos para tu entrada: ")
estatura = float (input ("Cuanto mides?: "))
edad = int (input ("Cual es tu edad?: "))
if estatura >= 1.70 and edad >= 18:
            print (nombre + " tienes acceso VIP a todas las atracciones.")
if estatura < 1.70 and edad >= 18:
            print (nombre + " tienes acceso General para adultos.")
if estatura >= 1.40 and edad < 18:
            print (nombre + " tienes acceso juvenil.")
if estatura < 1.40 and edad < 18:
            print (nombre + " no cumples con la estatura para ingresar.")
