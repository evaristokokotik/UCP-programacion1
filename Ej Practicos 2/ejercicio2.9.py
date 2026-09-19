#Realice un programa que calcule la nómina salarial neto, de unos obreros cuyo trabajo
#se paga en horas. El cálculo se realiza de la siguiente forma:
#a. Las primeras 35 horas a una tarifa fija.
#b. Las horas extras se pagan a 1.5 más de la tarifa fija.
#c. Los impuestos a deducir de los trabajadores varían, según el sueldo mensual
#si el sueldo es menos de $200.000 el sueldo es libre de impuesto y si es al
#contrario se cobrará un 20% de impuesto.

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa_fija = float(input("Ingrese la tarifa fija por hora: "))

if horas_trabajadas <= 35:
    sueldo_bruto = horas_trabajadas * tarifa_fija
else:
    horas_extras = horas_trabajadas - 35
    sueldo_bruto = (35 * tarifa_fija) + (horas_extras * tarifa_fija * 1.5)

if sueldo_bruto < 200000:
    sueldo_neto = sueldo_bruto
else:
    sueldo_neto = sueldo_bruto - (sueldo_bruto * 0.2)

print(f"El sueldo neto es: ${round(sueldo_neto, 2)}")

