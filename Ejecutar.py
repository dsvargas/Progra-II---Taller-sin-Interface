import random

x = 0  # Eje en x
y = 0
campos = 0  # El es total de campos que tiene la matriz
nombreJugador1 = ""  # Nombre del primer jugador
nombreJugador2 = ""  # Nombre del segundo jugador o de el compu
matrizJugador1 = []  # Matriz del jugador 1
matrizJugador2 = []  # Matriz del jugador
matrizJugadas1 = []  # Matriz jugadas
matrizJugadas2 = []  # Matriz jugadas
numElementos = 0  # cantidad de elementos que participan en la partida para ambos jugadores va a ser igual
win = False  # S guarda en false y cambia hasta que uno de los dos jugadores cambie
modalidad = 0  # Guarda si se juega con uno o con dos jugadores
barcos1 = 0
barcos2 = 0
fallos1 = 0
aciertos1 = 0
fallos2 = 0
aciertos2 = 0
fila = 0
columna = 0
# ########################################################################################################################
def popcion():  # funcion para imprimir las opciones de modalidad
    print("╔════════════════╗", "\n", "   1. Jugador vs Jugador", "\n", "   2. Jugador vs Computador")
    print("╚════════════════╝")


def pseleccion():  # funcion para imprimir la cantidad de elementos que requiere
    print("╔══════════════════════╗", "\n", "  Seleccionar la cantidad elementos ", "\n", "   mínimo 1 elementos por partida")
    print("╚══════════════════════╝")

def MatrizJuegador1():  # funcion imprime la matriz del jugador 1
    print("═════════ Jugador 1 ════════════")
    for i in matrizJugador1:  # recorre la matriz
        print(i)  # imprime las filas de la matriz
    print("════════════════════════════")


def MatrizJugador2():  # funcion q1ue imprime la matriz del jugador 2
    print("═════════ Jugador 2 ════════════")
    for i in matrizJugador2:  # recorre la matriz
        print(i)  # imprime las filas de la matriz
    print("════════════════════════════")


# ################################################################################################################
def matriz():
    global x
    global y
    global campos
    x = int(input("Digite la cantidad de filas: "))  # Cantidad de filas que tendra la mariz
    y = int(input("Digite la cantidad de columnas: "))  # Cantidad de columnas de la matriz
    if x <= 2 or y <= 2:  # Si la matriz es menor a 3x3 es muy pequeña entoncs se hace esta validacion de tamaño de la matriz
        print("Debe digitar un numero mayor a 2")
        matriz()
    campos = x * y  # Guarda el tamaño de la matriz para hacer una validacion de espacios luego
    for j in range(x):  # Hace hasta alcanzar el rango de x
        matrizJugador1.append([0] * y)  # crea los columnas el matriz jugador 1
        matrizJugador2.append([0] * y)  # crea los columnas el matriz jugador 2
        matrizJugadas1.append([0] * y)  # crea la matriz para visualizar jugadas de el jugador 1
        matrizJugadas2.append([0] * y)  # crea la matriz para visualizar jugadas de el jugador 2


def CantidadElementos():  # digita la cantidad de barcos y me valida que hayan mas de 1 elementos o uno
    # y que los elementos no sean mas que la mitad de todos los campos de la matriz
    pseleccion()
    global numElementos
    try:
        numElementos = int(input("Digite la cantidad de elementos: "))
    except:
        numElementos = int(input("Digite solo elementos numericos: "))

    while (numElementos <= 1) and (numElementos > campos // 2):  # La cantidad de elementos tiene que ser mayor a 1
        # y menor que la mitad del total de campos de la matriz
        try:
            numElementos = int(input("Digite la cantidad de elementos mayor 1: "))
        except:
            numElementos = int(input("Digite solo elementos numericos: "))


def colocarElementos():
    conta1 = 0
    conta2 = 0
    while conta1 < numElementos:  # coloca la cantidad de  elementos que el usuario ingreso
        try:
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
        except:
            print("Solo numeros")
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la fila donde quiere colocar el elemento "))

        if i < 0 or i > x or j < 0 or j > y:  # valida que no se salga de rango de la matriz
            print("Posicion invalida")
        elif matrizJugador1[i - 1][j - 1] != 0:
            print("Campo esta ocupado")
        else:
            matrizJugador1[i - 1][j - 1] = 1
            conta1 += 1
            MatrizJuegador1()

    if modalidad == 1:
        while conta2 < numElementos:
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
            if i < 0 or i > x or j < 0 or j > y:
                print("Posicion invalida")
            elif matrizJugador2[i - 1][j - 1] != 0:
                print("Campo esta ocupado")
            else:
                matrizJugador2[i - 1][j - 1] = 1
                conta2 += 1
                MatrizJugador2()
    else:
        while conta2 < numElementos:
            fila = random.randint(0, x - 1)
            columna = random.randint(0, y - 1)
            if matrizJugador2[fila][columna] == 0:
                matrizJugador2[fila][columna] = 1
                conta2 += 1


def turnos():
    win1 = False
    win2 = False
    jugador1 = False
    jugador2 = False
    global barcos1
    global barcos2

    while win1 == False and win2 == False:
        while jugador1 == False:
            print("Turno jugador ", nombreJugador1)
            fila = int(input("Indique la fila donde desea tirar la bomba: "))
            columna = int(input("Indique la columna donde desea tirar la bomba:"))
            if fila >= len(matrizJugador2) or columna >= len(matrizJugador2[0]):
                print("La posicion no es valida")
            else:
                jugador1 = ataque(1)
                if jugador1==False:
                    barcos1+=1
                    if(barcos1==numElementos):
                        win1=True
        if modalidad == 1:
            while jugador2 == False:
                print("Turno jugador ", nombreJugador2)
                fila = int(input("Indique la fila donde desea tirar la bomba: "))
                columna = int(input("Indique la columna donde desea tirar la bomba:"))
                if fila >= len(matrizJugador1) or columna >= len(matrizJugador1[0]):
                    print("La posicion no es valida")
                else:
                    jugador2 = ataque(2)
                    if jugador2==False:
                        barcos2+=1
                        if(barcos2==numElementos):
                            win2=True
        else:
            while jugador2 == False:
                print("Turno jugador  Computadora")
                fila = random.randint(0, x - 1)
                columna = random.randint(0, y - 1)
                if fila >= len(matrizJugador1) or columna >= len(matrizJugador1[0]):
                    print("La posicion no es valida")
                else:
                    jugador2 = ataque(2)
                    if jugador2==False:
                        barcos2+=1
                        if(barcos2==numElementos):
                            win2=True

def ataque(jugador):
    global aciertos1
    global fallos1
    global aciertos2
    global fallos2
    if jugador == 1:
        if matrizJugador2[fila][columna] == 1:
            matrizJugador2[fila - 1][columna - 1] = 0
            print("¡Blanco acertado!")
            aciertos1 += 1
            matrizJugadas1[fila][columna] = 2
            return False
        else:
            print("¡Blanco fallado!")
            fallos1 += 1
            return True
    else:
        if matrizJugador1[fila][columna] == 1:
            matrizJugador1[fila - 1][columna - 1] = 0
            print("¡Blanco acertado!")
            aciertos2 += 1
            matrizJugadas2[fila][columna] = 2
            return False
        else:
            print("¡Blanco fallado!")
            fallos2 += 1
            return True


def start():
    popcion()
    global modalidad
    global nombreJugador1
    global nombreJugador2
    try:
        modalidad = int(input("Presione la opcion  1/2: "))
    except:
        print("Digite solo elementos numericos")
        modalidad = int(input("presione la opcion 1/2: "))

    while (modalidad != 1) and (modalidad != 2):
        print("Digite una opcion valida")
        popcion()

    if modalidad == 1:
        nombreJugador1 = input("Seleccione el nombre del Jugador 1...")
        nombreJugador2 = input("seleccione el nombre del jugador 2...")
        matriz()
        CantidadElementos()
        colocarElementos()
    else:
        nombreJugador1 = input("Seleccione el nombre del Jugador 1...")
        matriz()
        CantidadElementos()
        colocarElementos()
    turnos()


start()