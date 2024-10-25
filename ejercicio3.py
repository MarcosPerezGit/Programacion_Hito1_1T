"""
Ejercicio 3:
Simular el funcionamiento de una cuenta bancaria (2.5 puntos): al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto.
Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos.
"""
#Inicializamos variables
saldo = 0
opcion = 0
ingresar = 0
retirar = 0
contador_ingresos = 0
contador_retiradas = 0
#Le damos la bienvenida y le pedimos que introduzca un saldo positivo
print(f"BIENVENIDO A NUESTRO BANCO")
saldo = float(input("INGRESE SU SALDO INICIAL:" ))
#Aqui creamos un bucle while con 5 opciones distintas
while opcion !=5:
        if (saldo > 0):
            print(f"1-Ingresar dinero\n2-Retirar dinero\n3-Mostrar Saldo\n4-Estadisticas\n5-Salir")
            opcion = int(input("ELIGE UNA OPCION: "))
            if (opcion == 1):
                ingresar = float(input("CUANTO QUIERES INGRESAR: "))
                if (ingresar > 0):              
                    saldo = saldo + ingresar
                    contador_ingresos = contador_ingresos + 1
                elif (ingresar < 0 ):                       #Aqui controlamos que el dinero que se ingresa no sea negativo
                    print(f"NO SE PUEDE AÑADIR SALDO NEGATIVO")

            elif (opcion == 2):
                retirar = float(input("CUANTO QUIERES RETIRAR: "))
                if(retirar < saldo):
                    saldo = saldo - retirar
                    contador_retiradas = contador_retiradas + 1
                elif (retirar > saldo):
                    print(f"NO TIENES EL DINERO QUE QUIERES RETIRAR")
            elif (opcion == 3):
                print(f"**********************")
                print(f"TU SALDO ACTUAL ES: {saldo}")
                print(f"**********************")
            elif (opcion == 4):
                print(f"HAS INGRESADO DINERO {contador_ingresos} VECES. ")
                print(f"HAS RETIRADO DINERO {contador_retiradas} VECES. ")
            elif(opcion == 5):
                print(f"HASTA PRONTO!!")
            else:
                print(f"INTRODUCE UNA OPCION VALIDA")
        else:
            print(f"INTRODUCE UN VALOR POSITIVO")
            saldo = float(input("INGRESE SU SALDO INICIAL:" ))