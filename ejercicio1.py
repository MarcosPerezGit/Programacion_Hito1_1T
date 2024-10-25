"""
Ejercicio 1:
Mostrar figuras por pantalla (2,5 puntos): a través de un menú solicitaremos al
usuario que tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no es
correcta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta.
"""
#Inicializamos variables
lado = 0
opcion = 0
area = 0
perimetro = 0

#Mostramos el menu
#Aqui creamos un bucle while para que cuando meta un numero distinto de 3 entre al bucle
while (opcion !=3):
    print(f"1-Cuadrado\n2-Rectángulo\n3-Salir")
    opcion = int(input("Selecciona una opcion del menu: "))
    #Aqui controlamos que el numero que nos da sea entre 1 y 3
    if (opcion >=1 and opcion<=3):
        #Esta es la opcion del cuadrado y calcula muestra el area y el perimetro
        if opcion == 1:
            lado = int(input("Dime cuanto mide el lado del Cuadrado "))
            area = lado * lado
            print(f"El area del cuadrado es: {area} ")
            perimetro = lado * 4
            print(f"El perimetro del cuadrado es: {perimetro} ")
            for i in range (lado):
                print(f"*"*lado)
    #Esta es la opcion del rectangulo y calcula muestra el area y el perimetro
        elif opcion == 2:
            base = int(input("Dime la base del rectangulo "))
            altura = int(input("Dime la altura del rectangulo "))
            area = base * altura
            print(f"El area del rectangulo es: {area} ")
            perimetro = (base * 2) + (altura * 2)
            print(f"El perimetro del rectangulo es: {perimetro} ")
            for i in range(altura):
                print(f"*"*base)
    #Si seleccionas la opcion 3 sales del sistema
        elif opcion == 3:
            print(f"SALIENDO DEL SISTEMA")
    #Este es un control para que cada vez que se escriba un numero no deseado te salte un error y te de otra oportunidad
    else:
        print(f"ERROR")