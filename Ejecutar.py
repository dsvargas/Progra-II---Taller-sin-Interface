import random

x = 0  # Eje en x
y = 0  # Eje en y
campos = 0  # El es total de campos que tiene la matriz
nombreJugador1 = ""  # Nombre del primer jugador
nombreJugador2 = ""  # Nombre del segundo jugador o de el compu
matrizJugador1 = []  # Matriz del jugador 1
matrizJugador2 = []  # Matriz del jugador
matrizJugadas1 = []  # Matriz jugadas
matrizJugadas2 = []  # Matriz jugadas
numElementos = 0  # cantidad de elementos que participan en la partida para ambos jugadores va a ser igual
win1 = False  # S guarda en false y cambia hasta que jugador 1 gane
win2 = False  # S guarda en false y cambia hasta que jugador 2 gane
modalidad = 0  # Guarda si se juega con uno o con dos jugadores
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
    print("╔══════════════════════╗", "\n", "  Seleccionar la cantidad elementos ", "\n",
          "   mínimo 1 elementos por partida")
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


def Matrizjugada1():
    print("═════════ Jugadas jugador 1 ════════════")
    for i in matrizJugadas1:  # recorre la matriz
        print(i)  # imprime las filas de la matriz


def Matrizjugada2():
    print("═════════ Jugadas jugador 2 ════════════")
    for i in matrizJugadas2:  # recorre la matriz
        print(i)  # imprime las filas de la matriz


# ################################################################################################################
def matriz():
    global x
    global y
    global campos
    try:
        x = int(input("Digite la cantidad de filas: "))  # Cantidad de filas que tendra la mariz
        y = int(input("Digite la cantidad de columnas: "))  # Cantidad de columnas de la matriz
    except:
        matriz()
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
        CantidadElementos()

    while (numElementos <= 1) and (numElementos < campos // 2):  # La cantidad de elementos tiene que ser mayor a 1
        # y menor que la mitad del total de campos de la matriz
        try:
            numElementos = int(input("Digite la cantidad de elementos mayor 1: "))
        except:
            print("Digite solo elementos numericos: ")
            CantidadElementos()


def colocarElementos():
    conta1 = 0  # cuenta cuantos barcos a colocado el jugador 1
    conta2 = 0  # cuenta cuantos barcos a colocado el jugador 2
    while conta1 < numElementos:  # coloca la cantidad de  elementos que el usuario ingreso
        try:
            print("Jugador: ",nombreJugador1)
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
        except:
            print("Solo numeros")
            colocarElementos()

        if i < 0 or i > x or j < 0 or j > y:  # valida que no se salga de rango de la matriz #########################################
            print("Posicion invalida")
        elif matrizJugador1[i - 1][j - 1] != 0:  # Si ya hay un elemento en esa posicion no deja colocarlo
            print("Campo esta ocupado")
        else:
            matrizJugador1[i - 1][j - 1] = 1  # Si el campo esta vacio y no se sale del rango coloca el elemnto
            conta1 += 1  # Coloco un elemeto ya
            MatrizJuegador1()  # vista de la matriz del jugador

    if modalidad == 1:  # si modalidad es igual a uno quiere decir que hay dos jugadores
        while conta2 < numElementos:  # Mientras el contador sea menor que el num de elmentos
            print("Jugador: ",nombreJugador2)  # Nombre del jugador
            try:
                i = int(input("Digite la fila donde quiere colocar el elemento "))
                j = int(input("Digite la columna donde quiere colocar el elemento "))
            except:
                print("Digite valores numericos")
            if (i < 0) or (i > x) or (j < 0) or (j > y):
                print("Posicion invalida")
            elif matrizJugador2[i - 1][j - 1] != 0:  # Si ya hay un elemento en esa posicion no deja colocarlo
                print("Campo esta ocupado")
            else:
                matrizJugador2[i - 1][j - 1] = 1 # Si el campo esta vacio y no se sale del rango coloca el elemnto
                conta2 += 1  # aumenta el contador
                MatrizJugador2()  # Vista de la matriz del jugador
    else:
        while conta2 < numElementos:  # Cuando el segundo jugador es la compu coloca los elementos a lo ramdom
            fila = random.randint(0, x - 1)  # define una fila a lo random
            columna = random.randint(0, y - 1)  # define una columna a lo random
            if matrizJugador2[fila][columna] == 0:  #si la columna y la fila es un campo vacio
                matrizJugador2[fila][columna] = 1  # le coloca un 1 en esa fila y columna
                conta2 += 1 # aumenta el contador
        MatrizJugador2()  # Vista de la matriz del jugador


def turnos():
    global modalidad
    global aciertos1
    global aciertos2
    global fila
    global columna
    global win1
    global win2
    jugador1 = False
    jugador2 = False  # utilizadas para saber el turno del juegador

    while win1 == False and win2 == False:  # Mientras ninguno de los dos jugadores hayan ganado
        jugador2 = False
        while jugador1 == False and win1 == False and win2 == False:  # Mientras jugador dos no haya ganado
            print("Turno jugador ", nombreJugador1)  # Nombre del jugador 1
            Matrizjugada1()  # Imprime una matriz para ver donde se van colocando las bombas
            try:
                fila = int(input("Indique la fila donde desea tirar la bomba: "))  # Indica la fila donde se coloca la bomba
                columna = int(input("Indique la columna donde desea tirar la bomba:"))  # Indica la columna donde se coloca la bomba
            except:
                print("Digite solo elementos")
            if fila > len(matrizJugador2) or columna > len(matrizJugador2[0]) or fila == 0 or columna == 0:  # Si se sale de el rango de la matriz
                print("La posicion no es valida")  # no hace nada
            else:  # si entra en el rango de la matriz
                if jugador1 == False:  # le da permiso al jugador1 para poner la bomba
                    jugador1 = ataque(1)  # ver si el jugador acerto y llama a ataque
                    if (aciertos1 == numElementos):  # si los aciertos de el jugador 1 y el nimero de elementos es igual
                        win1 = True  # le da el gane a jugador 1
                        break

        jugador1 = False
        if (modalidad == 1) and (win1 == False) and (win2 == False):  # mientras jugador uno no haya ganado
            while jugador2 == False:  # le da permiso para jugar al jugador 2
                print("Turno jugador ", nombreJugador2)  # nombre del jugador
                Matrizjugada2() # Imprime una matriz para ver donde se colocan las bombas
                try:
                    fila = int(input("Indique la fila donde desea tirar la bomba: "))  # Indica la fila donde se coloca la bomba
                    columna = int(input("Indique la columna donde desea tirar la bomba:"))  # Indica la columna donde se coloca la bomba
                except:
                    print("Solo elementos numericos")
                if fila > len(matrizJugador1) or columna > len(matrizJugador1[0]):  # si se sale de el rango de la matriz
                    print("La posicion no es valida")  # no hace nada
                else:  # si entra en el rango de la matriz
                    if jugador2 == False:  # le da permiso al jugador 2 para poner la bomba
                        jugador2 = ataque(2)  #ver si el jugador acerto y llama a ataque
                    if (aciertos2 == numElementos):
                        win2 = True
                        break
        else:
            while jugador2 == False and win1 == False and win2 != True:
                print("Turno jugador  Computadora")
                fila = random.randint(1, x - 1)
                columna = random.randint(1, y - 1)
                if fila > len(matrizJugador1) or columna > len(matrizJugador1[0]):
                    print("La posicion no es valida")
                elif matrizJugadas2[fila - 1][columna - 1] != 2:
                    jugador2 = ataque(2)
                    if jugador2 == False:
                        if (aciertos2 == numElementos):
                            win2 = True
                            break
    estadisticas()


def ataque(jugador):
    global aciertos1
    global fallos1
    global aciertos2
    global fallos2
    global fila
    global columna
    if jugador == 1:  # Indica de quien es el turno para jugar
        if matrizJugador2[fila - 1][columna - 1] == 1:  # Revisa la posicion de la matriz para ver si hay barcos
            matrizJugador2[fila - 1][columna - 1] = 0  # si lo encuentra lo cambia por un 0
            print("¡Blanco acertado!")  # si le dio al barco
            aciertos1 += 1  # si el jugador1 acierta el blanco
            matrizJugadas1[fila - 1][columna - 1] = 2  # me dice donde coloque una bomba
            return False  # retorna false si acierta un barco, para que siga jugando el jugador actual
        else:  # Fallo el blanco
            print("¡Blanco fallado!")
            fallos1 += 1  # aumenta el contador de fallos de el jugador 1
            matrizJugadas1[fila - 1][columna-1] = 2
            return True  # retorna true para que juegue el otro jugador
    else:  # turno del segundo jugador
        if matrizJugador1[fila - 1][columna - 1] == 1:  # Revisa la posicion de la matriz para ver si hay barcos
            matrizJugador1[fila - 1][columna - 1] = 0  # si lo encuentra lo cambia por 0
            print("¡Blanco acertado!")  # si le dio al barco
            aciertos2 += 1  # si el jugador 2 acierta
            matrizJugadas2[fila - 1][columna - 1] = 2  # me dice donde coloque la bomba
            return False  # retorna false para que siga jugando el jugador 2
        else:  # Fallo el blanco
            print("¡Blanco fallado!")
            fallos2 += 1  # si el jugador falla el blanco
            matrizJugadas2[fila - 1][columna - 1] = 2  # Aunque el blanco falle o acierte coloca donde callo
            return True  # true para que pase al sig jugador


def estadisticas():
    global win1
    global win2

    if win1 == True:
        print("╔══════════════════════╗","\n", "   VICTORIA",nombreJugador1,"\n","   Cantidad de aciertos: ",aciertos1,"\n","   Cantidad de Fallos: ",fallos1,"\n","   DERROTA ",nombreJugador2,"\n","   Cantidad de aciertos: ",aciertos2,"\n","   Cantidad de Fallos: ",fallos2)
        print("╚══════════════════════╝")
    elif win2 == True:
        if modalidad == 2:
            print("╔══════════════════════╗","\n", "   VICTORIA"," Computador", "\n", "   Cantidad de aciertos: ",aciertos2,"\n","   Cantidad de Fallos: ",fallos2,"\n", "   DERROTA ",nombreJugador1,"\n","   Cantidad de aciertos: ",aciertos1)
            print("╚══════════════════════╝")
        else:
            print("╔══════════════════════╗","\n", "   VICTORIA",nombreJugador2, "\n", "   Cantidad de aciertos: ",aciertos2,"\n","   Cantidad de Fallos: ",fallos2,"\n", "   DERROTA ",nombreJugador1,"\n","   Cantidad de aciertos: ",aciertos1)
            print("╚══════════════════════╝")
    else:
        print("Cosita")
        print("   VICTORIA",nombreJugador1,"\n","   Cantidad de aciertos: ",aciertos1,"\n","   Cantidad de Fallos: ",fallos1)
        print("   VICTORIA",nombreJugador2,"\n","   Cantidad de aciertos: ",aciertos2,"\n","   Cantidad de Fallos: ",fallos2)


def start():
    popcion()
    global modalidad
    global nombreJugador1
    global nombreJugador2
    global x
    global y   
    global campos
    global matrizJugador1 
    global matrizJugador2  
    global matrizJugadas1 
    global matrizJugadas2 
    global numElementos  
    global win1 
    global win2  
    global fallos1
    global aciertos1 
    global fallos2 
    global aciertos2
    global fila
    global columna
    
    try:
        modalidad = int(input("Presione la opcion  1/2: "))
        if modalidad != 1 and modalidad != 2:
            print("opcion invalida")
            start()
    except:
        print("Digite solo elementos numericos")
        modalidad = int(input("presione la opcion 1/2: "))
        if modalidad != 1 and modalidad != 2:
            print("opcion invalida")
            start()

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
    nulo = input("presione cualquier tecla para volver a empezar")
    x = 0  
    y = 0  
    campos = 0  
    nombreJugador1 = ""  
    nombreJugador2 = ""  
    matrizJugador1 = [] 
    matrizJugador2 = [] 
    matrizJugadas1 = []  
    matrizJugadas2 = []  
    numElementos = 0  
    win1 = False  
    win2 = False  
    modalidad = 0 
    fallos1 = 0
    aciertos1 = 0
    fallos2 = 0
    aciertos2 = 0
    fila = 0
    columna = 0
    start()

start()
