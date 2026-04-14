# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
  def main():
    nombre = input()

    archivo = open(nombre, "r")

    linea = archivo.readline()
    n = int(linea.strip())

    timer = lap_timer.init(n)

    for linea in archivo:
        tiempo = float(linea.strip())
        lap_timer.add_lap(timer, tiempo)

    archivo.close()

    print(lap_timer.longest_decreasing_streak(timer))

if __name__ == "__main__":
    main()
