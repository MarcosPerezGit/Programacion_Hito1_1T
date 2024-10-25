"""
Ejercicio 2:
El usuario introduce un valor (1-
Piedra|2- Papel|3-Tijera), si no es correcto se volver a pedir de nuevo hasta que se correcta.
La “maquina” generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Al
finalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o
empatado.
"""
#Importamos libreria Random
import random
#Inicializamos variables
opcion = 0
aleatorio = random.randint(1,3)
victorias = 0
derrotas = 0

#Creamos un bucle while diciendole que mientras el contador de victorias y derrotas sean distintos a 3, puede entrar
while victorias != 3 or derrotas != 3:
    print(f"1-Piedra\n2-Papel\n3-Tijera")
    opcion = int(input("Selecciona una opcion "))
#Aqui se controla que si la opcion seleccionada y la aleatoria son iguales, quede en empate
    if opcion == aleatorio:
        print(f"Has empatado")
        print(f"HABEIS ELEGIDO LO MISMO")
#Aqui se compara las posibilidades entre piedra y papel
    if opcion == 1 and aleatorio == 2:
        print(f"Has seleccionado Piedra")
        print(f"El enemigo ha seleccionado Papel")
        print(f"Has perdido")
        derrotas = derrotas + 1
#Aqui se compara las posibilidades entre piedra y tijeras
    elif opcion == 1 and aleatorio == 3:
        print(f"Has seleccionado Piedra")
        print(f"El enemigo ha seleccionado Tijeras")
        print(f"Has ganado")
        victorias = victorias + 1
#Aqui se compara las posibilidades entre papel y piedra
    if opcion == 2 and aleatorio == 1:
        print(f"Has seleccionado Papel")
        print(f"El enemigo ha seleccionado Piedra")
        print(f"Has ganado")
        victorias = victorias + 1
#Aqui se compara las posibilidades entre papel y tijeras
    elif opcion == 2 and aleatorio == 3:
        print(f"Has seleccionado Papel")
        print(f"El enemigo ha seleccionado Tijeras")
        print(f"Has perdido")
        derrotas = derrotas + 1
#Aqui se compara las posibilidades entre tijeras y piedra
    elif opcion == 3 and aleatorio == 1:
        print(f"Has seleccionado Tijeras")
        print(f"El enemigo ha seleccionado Piedra")
        print(f"Has perdido")
        derrotas = derrotas + 1
#Aqui se compara las posibilidades entre tijeras y papel
    elif opcion == 3 and aleatorio == 2:
        print(f"Has seleccionado Tijeras")
        print(f"El enemigo ha seleccionado Papel")
        print(f"Has ganado")
        victorias = victorias + 1
#Aqui se compara victorias y derrotas, y si alguno de los dos llega a 3, se muestra el final y acaba el juego
    if (victorias == 3):
        print(f"HAS GANADO 3 ASALTOS, ENHORABUENAAA")
        break
    elif (derrotas == 3):
        print(f"HAS PERDIDO 3 ASALTOS, QUE MALO ERES")
        break