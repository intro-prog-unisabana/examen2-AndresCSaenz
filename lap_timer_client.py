# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
    nombre = input("Nombre del archivo: ")

    timer = lap_timer.init()

    archivo = open(nombre, "r")

    for linea in archivo:
        tiempo = float(linea.strip())
        lap_timer.add_lap(timer, tiempo)

    archivo.close()
    
    print(lap_timer.longest_decreasing_streak(timer))



if __name__ == "__main__":
    main()
