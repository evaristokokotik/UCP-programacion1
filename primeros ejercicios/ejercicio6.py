#Escribir un algoritmo que permita loguearse (registrarse) a un sistema, ingresando un
#nombre de usuario y la contraseña adecuada. Considerar que tanto el usuario como la 
#contraseña están formados sólo por letras. El sistema deberá validar que el usuario y la
#contraseña sean correctas, comparándolas con lo que el sistema tiene registrado para ese usuario.

usuario = "usuario"  # Usuario registrado en el sistema
contraseña = "contraseña"  # Contraseña registrada en el sistema

usuario_ingresado = input("Ingrese su nombre de usuario: ")
contraseña_ingresada = input("Ingrese su contraseña: ")

if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
    print("Inicio de sesión exitoso.")
else:
    print("Nombre de usuario o contraseña incorrectos.")