#¿ Alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"] pero yo quiero saber si esos estan o no estan regular ?

#¿ Que dictamina si un alumno esta o no esta regular ?

#Necesitamos tener las 4 notas alumnos para poder determinar si estan regulares o no.

#Y saber el % de asistencia de cada alumno.

alumnos = { nombre: "Juan", notas: [7, 8, 9, 6], asistencia: 90 }, 
{ nombre: "Maria", notas: [5, 6, 4, 7], asistencia: 60 }, 
{ nombre: "Pedro", notas: [1, 9, 4, 7], asistencia: 95 },
{ nombre: "Ana", notas: [6, 5, 7, 8], asistencia: 85 } 

#hacer una funcion que determine si cada alumno esta regular o no, y que muestre el resultado en pantalla.

def determinar_regularidad(alumnos):
    for alumno in alumnos:
        nombre = alumno['nombre']
        notas = alumno['notas']
        asistencia = alumno['asistencia']

        promedio_notas = sum(notas) / len(notas)
        
        if promedio_notas >= 6 and asistencia >= 75:
            estado = "regular"
        else:
            estado = "no regular"

        print(f"El alumno {nombre} está {estado}. Promedio de notas: {promedio_notas:.2f}, Asistencia: {asistencia}%")





