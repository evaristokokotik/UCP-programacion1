#Programa que lea 3 números los cuales significan una fecha (día, mes, año). Comprobar que
#sea válida la fecha, si no es válido que imprima un mensaje de error, y si es válida mostrar
#la fecha completa con el siguiente formato “dd/mes/año” .
#Validaciones
#a. Si el día es mayor a 31, el mes mayor a 12 o el año menor que cero es incorrecto.
#b. Los meses Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre tienen 31 días.
#c. Febrero tiene 28 días
#d. Los meses Abril, Junio, Septiembre, Noviembre tienen 30 días.

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if dia < 1 or dia > 31 or mes < 1 or mes > 12 or año < 0:
    print("Fecha incorrecta. Por favor, ingrese una fecha válida.")
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31:
    print(f"La fecha completa es: {dia}/{mes}/{año}")
elif mes == 2 and dia <= 28:
    print(f"La fecha completa es: {dia}/{mes}/{año}")
elif mes in [4, 6, 9, 11] and dia <= 30:
    print(f"La fecha completa es: {dia}/{mes}/{año}")
else:
    print("Fecha incorrecta. Por favor, ingrese una fecha válida.")

