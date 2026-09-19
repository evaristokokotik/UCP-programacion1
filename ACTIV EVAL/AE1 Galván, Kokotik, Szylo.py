# Programa de un cajero automático en python (AE1)
# Saldo inicial predeterminado de $50.000
saldo = 50000
opcion = 0

usuarioregistrado = "admin"  # Usuario registrado en el sistema
claveregistrada = "admin"  # Contraseña registrada en el sistema

acceso = False  # Variable para controlar el acceso al sistema


while not acceso:  # Bucle para permitir múltiples intentos de inicio de sesión hasta que se ingrese correctamente

    print("+++ INICIO DE SESIÓN +++")
    usuarioingresado = input("Ingrese su nombre de usuario: ")  #pedimos al usuario que ingrese su nombre de usuario
    claveingresada = input("Ingrese su contraseña: ")   #pedimos al usuario que ingrese su contraseña

    # Validación de credenciales
    if usuarioingresado == usuarioregistrado and claveingresada == claveregistrada:
        print("| ACCESO OTORGADO |")
        acceso = True  # Se otorga acceso al sistema

        # Bucle para mantener el menú interactivo activo hasta que el usuario elija salir (opción 4)
        while opcion != 4:
            print("       MENU DE OPCIONES          ")
            print("1. Consultar saldo disponible.")
            print("2. Depositar dinero.")
            print("3. Extraer dinero.")
            print("4. Salir.")
            
            # Pedimos al ususario que seleccione una opción del menú
            opcion = int(input("Elija una opción (1-4): "))
            
            if opcion == 1:
                print("Su saldo actual es: $", saldo)   #mostrar por pantalla el saldo actual
                
            elif opcion == 2:
                monto = float(input("Ingrese el monto a depositar: "))  
                if monto > 0:   # Validación de que el monto a depositar sea mayor a 0
                    saldo = saldo + monto   # Se suma el monto depositado al saldo actual
                    print("Se ha depositado el monto de forma exitosa. Su saldo actual es: $", saldo)   # Se muestra el saldo actualizado después del depósito
                else:
                    print("ERROR: El monto a depositar debe ser mayor a 0 (cero).")
                    
            elif opcion == 3:
                monto = float(input("Ingrese el monto a extraer: "))
                # Validación de fondos suficientes
                if monto <= saldo and monto > 0:
                    saldo = saldo - monto
                    print("Extracción realizada con éxito. Saldo restante: $", saldo)
                elif monto > saldo:     # Validación de fondos insuficientes 
                    print("Fondos insuficientes para realizar la operación")
                else:   # Validación de que el monto a extraer sea mayor a 0
                    print("ERROR: Ingrese un monto válido.")
                    
            elif opcion == 4:   # Validación de salida del programa
                print("¡Gracias por utilizar nuestros servicios!")
                
            else:   # Validación de opción inválida
                print("Opción inválida. Por favor, elija una opción entre 1 y 4.")
                
            print() # Línea en blanco para separar visualmente las iteraciones

    else:
        print("ERROR: Nombre de usuario o contraseña incorrectos.")
        
