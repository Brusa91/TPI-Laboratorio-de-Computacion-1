# Brusadin Leonardo Andrés.

# Para nuestro juego de Black Jack necesitamos importar el módulo random de Python.
import random

def barajaNueva(numero):
    """Defino una función para crear una baraja nueva."""
    if numero == 1:
        picas = []
        corazones = []
        trebol = []
        diamante = []
        baraja = [picas, corazones, trebol, diamante]
        palos = [ "♠" , "♥", "♣", "♦"]
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for palo in palos:
            #print(palo)
            if palo == "♠":
                for valor in valores:
                    valor += palo
                    picas.append(valor)
            elif palo == "♥":
                for valor in valores:
                    valor += palo
                    corazones.append(valor)
            elif palo == "♣":
                for valor in valores:
                    valor += palo
                    trebol.append (valor)
            else:
                for valor in valores:
                    valor += palo
                    diamante.append (valor)
    return baraja

def repartir(baraja , mano, valor):
    """ Defino una función para repartir una carta al azar.
    
    Me devuelve una lista con la baraja actualizada, la carta, el valor numérico de la carta, la cantidad de Jotas y de Ases de mi mano. 
    """
    # Selecciono una carta al azar.
    palo = random.choice(baraja)
    carta =str(random.choice(palo))
    valor.append(valorCarta(carta))
    mano.append(carta)
    # Elimino la carta de las disponibles en la baraja.
    palo.remove(carta)
    #print(valor)
    return baraja , mano , valor

def valorCarta(carta):
    """Defino una función para obtener el valor numérico de mi string carta."""
    valor = 0
    if carta[0] == "A":
        valor = 1
    elif carta [0] == "J" or carta[0] == "Q" or carta[0] == "K":
        valor = 10
    else:
        if len(carta) == 3:
            # Recorto mi cadena desde el índice 0 al 1 inclusive.
            valor = int(carta[0:2:1])
        elif len(carta) == 2:
            valor = int(carta[0])
    return valor

def puntosMano(valores, puntos):
    """Defino una función que calcule los puntos de mi mano."""
    for x in valores:
        puntos += x    
    return puntos

def esBlackJack(puntos, mano):
    """Defino una función que evalúa el puntaje para saber si es Black Jack."""
    blackJack = 0
    if puntos == 21 and len(mano) == 2:
        blackJack = 1
        return blackJack 

def nuevaPartida(k):
    """Defino una función para iniciar una nueva partida.
    
    k = 0 es el parámetro elegido para llamar la función."""
    while k == 0: 
        partida = int(input(f"Ingrese 1 para jugar otra vez o 2 para salir: "))
        if partida == 1:
            k = 1
        elif partida == 2:
            k = 1
        else:
            print(f"El valor {partida} ingresado no es válido.")
    return partida        

# Cargo mis condiciones iniciales y doy condiciones para una nueva partida.
partida = 1
while partida == 1:
    k = 0
    partida = 0
    baraja = barajaNueva(1)

    # Obtengo la mano del crupier.
    manoCrupier = []
    valoresCrupier = []
    manoCrupier = []
    puntosCrupier = 0

    repartir(baraja, manoCrupier, valoresCrupier)
    repartir(baraja, manoCrupier, valoresCrupier)
    print(f"La mano del crupier es:")
    i = 0
    while i == 0:
        for x in manoCrupier:
            print( x, end=" ")
        print()        
        puntosCrupier = puntosMano(valoresCrupier , puntosCrupier)
        if puntosCrupier == 21:
            i = 1
        """Decido qué valor toma el As del crupier en base a su puntaje.
    
            El As del crupier vale 1 sólo cuando se pasa de 21."""
        for j in range(len(valoresCrupier)):
            if valoresCrupier[j] == 1:
                puntosCrupier += 10
                if puntosCrupier > 21:
                    puntosCrupier -= 10
        """El crupier está obligado a tomar carta si su puntaje <= 16 y a detenerse si su puntaje >= 17."""
        if puntosCrupier >= 17:
            i = 1
        else:
            puntosCrupier = 0
            repartir(baraja, manoCrupier, valoresCrupier)

    blackJackCrupier = esBlackJack(puntosCrupier, manoCrupier)
    print(f"Los puntos del crupier son: {(puntosCrupier)}\n")
    if puntosCrupier > 21:
        print(F"\n GANASTE!\n El crupier se pasó de 21\n")
        partida = nuevaPartida(k)   
    if  partida == 1:
        continue
    elif partida == 2:
        break

    # Obtengo la mano del jugador.
    cartasJugador = []
    valoresJugador = []
    manoJugador = []
    puntosJugador = 0
    repartir(baraja, manoJugador, valoresJugador)
    repartir(baraja, manoJugador, valoresJugador)
    print(f"La mano del jugador es: ")
    j = 0
    while j == 0:
        for x in manoJugador:
            print(x, end = " ")
        print()
        for i in range(len(valoresJugador)): 
            if valoresJugador [i] == 1:   
                valoresJugador[i] = int(input(f"Elija qué valor le da al As. Las opciones son 1 y 11: "))
        
        puntosJugador = (puntosMano(valoresJugador , puntosJugador))
        print(f"Los puntos del jugador son: {puntosJugador}\n")
        z = 0
        while z == 0:
            decision = int(input(f"Ingrese 1 para pedir otra carta, 2 para detenerse: "))
            if decision == 2:
                j = 1
                z = 1
            elif decision == 1:
                puntosJugador = 0
                repartir(baraja, manoJugador, valoresJugador)
                z = 1
            else:
                print("El valor ingresado no es válido.")    

    blackJackJugador = esBlackJack(puntosJugador, manoJugador)
    if puntosJugador > 21:
        print(F"\n PERDISTE!\n  Te pasaste de 21\n")
        partida = nuevaPartida(k)
    if  partida == 1:
        continue
    elif partida == 2:
        break
    
    # Comparamos resultados si ninguno de los dos se pasó de 21.

    if puntosJugador == puntosCrupier and blackJackCrupier == blackJackJugador == 1:
        print(f"\n El jugador y el crupier EMPATAN!\n Ambos tienen BALCK JACK!")
        partida = nuevaPartida(k)
    if  partida == 1:
        continue
    elif partida == 2:
        break
    elif blackJackCrupier == 0 and blackJackJugador == 0:
        if puntosCrupier == puntosJugador:
            print(f"\n EMPATAN!\n Ambos tienen {puntosCrupier} puntos.")
            partida = nuevaPartida(k)
        elif blackJackCrupier == 1 and blackJackJugador == 0:
            print(f"\n El crupier tiene \n BLACK JACK!\n PERDISTE!")
            partida = nuevaPartida(k)
        elif blackJackJugador == 1 and blackJackCrupier == 0:
            print(f"\n El jugador tiene \n BLACK JACK!\n GANASTE!")
            partida = nuevaPartida(k)
        elif puntosJugador > puntosCrupier:
            print(f"\n GANASTE!\n")
            partida = nuevaPartida(k)
        elif puntosCrupier > puntosJugador:
            print(f"\n El crupier gana con {puntosCrupier} puntos.\n PERDISTE!")
            partida = nuevaPartida(k)
        else:
            print("Ké")

    if  partida == 1:
        continue
    elif partida == 2:
        break        