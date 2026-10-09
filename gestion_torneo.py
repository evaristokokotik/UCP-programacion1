#Objetivos de la semana: Introducir la estructura de datos en memoria mediante arreglos unidimensionales (vectores). 
# Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido.

#Ningún torneo empieza con los jugadores ya anotados por arte de magia. 
# Nuestro sistema necesita un módulo de inscripción para que el juez registre 
# a los competidores antes de repartir puntos.

#Para poder poner en marcha el torneo, lo primero que necesitamos del sistema es
#poder cargar a los jugadores y luego armar las parejas que van a
#competir. Recuerden que en el pádel se juega de a dos: ninguna pareja puede
#tener más ni menos de 2 jugadores.

#a) Ingreso de jugadores

#Al iniciar el programa, el sistema debe preguntarle al juez: "¿Cuántos jugadores van a participar en el torneo?".
# A partir de esa respuesta, debe permitir registrar cada competidor, uno por uno, con la siguiente información:
# su nombre (con el que se lo identificará dentro del torneo), y
# su categoría (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

#b) Armado de parejas

# Una vez cargados todos los jugadores, el sistema debe permitir formar las parejas del torneo.
# Cada pareja debe tener:
# un nombre que la identifique dentro del torneo (por ejemplo,"Los Tanos"), 
# y exactamente 2 jugadores, elegidos entre los que ya fueron inscriptos.

import json

def cargar_jugadores():
    jugadores = []
    cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo? "))
    
    for i in range(cantidad_jugadores):
        nombre = str(input(f"Ingrese el nombre del jugador {i + 1}: "))
        categoria = (input(f"Ingrese la categoría del jugador {i + 1} (por ejemplo, 4ª, 5ª o 6ª): "))
        jugador = {"nombre": nombre, "categoria": categoria}
        jugadores.append(jugador)
    return jugadores

def guardar_jugadores(jugadores):
    with open("jugadores.json", "w", encoding="utf-8") as archivo:
        json.dump(jugadores, archivo, ensure_ascii=False, indent=4)

def leer_jugadores():
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def armar_parejas(jugadores):
    parejas = []
    cantidad_parejas = len(jugadores) // 2

    for i in range(cantidad_parejas):
        nombre_pareja = str(input(f"Ingrese el nombre de la pareja {i + 1}: "))
        jugador1 = jugadores[i * 2]
        jugador2 = jugadores[i * 2 + 1]
        parejas.append({"nombre": nombre_pareja, "jugadores": [jugador1, jugador2]})
    return parejas

def guardar_parejas(parejas):
    with open("parejas.json", "w", encoding="utf-8") as archivo:
        json.dump(parejas, archivo, ensure_ascii=False, indent=4)

def main():
    jugadores = cargar_jugadores()
    guardar_jugadores(jugadores)
    jugadores = leer_jugadores()

    print("\nJugadores registrados:")
    for jugador in jugadores:
        print(f"Nombre: {jugador['nombre']}, Categoría: {jugador['categoria']}")

    parejas = armar_parejas(jugadores)
    guardar_parejas(parejas)
    print("\nParejas formadas:")
    for pareja in parejas:
        nombres_jugadores = ", ".join([jugador["nombre"] for jugador in pareja["jugadores"]])
        print(f"Pareja: {pareja['nombre']}, Jugadores: {nombres_jugadores}")

main()

