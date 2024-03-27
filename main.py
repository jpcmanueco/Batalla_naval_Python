# main.py

from tablero import Tablero
from funciones import mostrar_tablero, colocar_barcos_jugador, colocar_barcos_bot, realizar_disparo, turno_maquina, verificar_fin_juego
from variables import barco_tamaños

def main():
    tamaño = 10
    tablero_jugador = Tablero(tamaño)
    tablero_bot = Tablero(tamaño)

    print("¡Bienvenido a Batalla Naval!")
    nivel_dificultad = int(input("Selecciona el nivel de dificultad (1: Fácil, 2: Medio, 3: Difícil): "))
    while nivel_dificultad not in [1, 2, 3]:
        nivel_dificultad = int(input("Nivel de dificultad inválido. Por favor, selecciona 1, 2 o 3: "))
    colocar_barcos_jugador(tablero_jugador)
    colocar_barcos_bot(tablero_bot)
    jugador_turno = True

    while True:
        if jugador_turno:
            print("\nTurno del jugador:")
            print("Opciones:")
            print("1. Realizar disparo")
            print("2. Mostrar tablero del jugador")
            print("3. Mostrar tablero del bot")
            print("4. Salir del juego")
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                mostrar_tablero(tablero_bot)
                try:
                    fila = int(input("Ingrese la fila para disparar: "))
                    columna = int(input("Ingrese la columna para disparar: "))
                    acierto = realizar_disparo(fila, columna, tablero_bot)
                    mostrar_tablero(tablero_bot)
                    if verificar_fin_juego(tablero_bot):
                        print("¡El jugador ha ganado!")
                        break
                    if not acierto:
                        jugador_turno = False
                except (ValueError, IndexError):
                    print("¡Coordenadas inválidas! Inténtalo de nuevo.")
            elif opcion == 2:
                mostrar_tablero(tablero_jugador)
            elif opcion == 3:
                mostrar_tablero(tablero_bot)
            elif opcion == 4:
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
        else:
            print("\nTurno del bot:")
            if nivel_dificultad == 1:
                acierto = turno_maquina(tablero_jugador)
            elif nivel_dificultad == 2:
                for _ in range(2):
                    acierto = turno_maquina(tablero_jugador)
                    if acierto:
                        break
            elif nivel_dificultad == 3:
                for _ in range(3):
                    acierto = turno_maquina(tablero_jugador)
                    if acierto:
                        break
            if not acierto:
                jugador_turno = True

if __name__ == "__main__":
    main()

