#Programa que lea 3 números los cuales significan una fecha (día, mes, año). Comprobar que
#sea válida la fecha, si no es válido que imprima un mensaje de error, y si es válida mostrar
#la fecha completa con el siguiente formato "dd/mes/año" .Validaciones
#a. Si el día es mayor a 31, el mes mayor a 12 o el año menor que cero es incorrecto.
#b. Los meses Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre tienen 31 días.
#c. Febrero tiene 28 días
#d. Los meses Abril, Junio, Septiembre, Noviembre tienen 30 días

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

valido = True
if dia < 1 or dia > 31 or mes < 1 or mes > 12 or año < 0:
    valido = False 
elif mes in [4, 6, 9, 11] and dia > 30:
    valido = False
    if dia > 30:
        valido = False
elif mes == 2 and dia > 28:
    valido = False

if valido:
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    print(f"La fecha completa es: {dia}/{meses[mes-1]}/{año}")
else:
    print("Fecha inválida. Por favor, ingrese una fecha correcta.")
