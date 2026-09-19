#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo
#por hora. Después debe mostrar por pantalla le pago que le corresponde.

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))
pago = horas_trabajadas * costo_por_hora
print("El pago correspondiente es:", pago)