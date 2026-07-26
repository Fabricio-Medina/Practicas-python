nombre = input ("Bienvenido(a), Cual es tu nombre?: ")
print ("Me da gusto que estes aqui " + nombre + " vamos a revisar tu promedio")
print ("Para empezar necesito las siguientes calificaciones: ")
matematicas = float (input (nombre + " Cual es tu calificacion en matematicas?: "))
fisica = float (input (nombre + " Cual es tu calificacion en fisica?: "))
geografia = float (input (nombre + " Cual es tu calificacion en geografia?: "))
promedio = (matematicas + fisica + geografia) / 3
if promedio >= 9:
    print (nombre +  " felicidades, tienes un promedio excelente de: ", round (promedio, 2))
if promedio >= 7 and promedio < 9:
    print (nombre +  " felicidades, tienes un promedio intermedio de: ", round (promedio, 2))
if promedio >= 6 and promedio < 7:
    print (nombre +  " felicidades tienes un promedio de: ", round (promedio, 2))
if promedio < 6:
     print (nombre + "  lo lamentamos, estas reprobado con un promedio de: ", round(promedio, 2))
