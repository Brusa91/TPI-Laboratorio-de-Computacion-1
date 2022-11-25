# Brusadin Leonardo Andrés.
# Legajo 15535.

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
    
    Me devuelve una lista con la baraja actualizada, la carta y el valor numérico de la carta. 
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
        if puntos == 21:
            continue
        if x == 1:
            puntos -= x    
            x = int(input(f"Elija qué valor le da al As. Las opciones son 1 y 11: "))
            puntos += x
    return puntos

# Cargo mis condiciones iniciales.

baraja = barajaNueva(1)

cartasJugador = []
valoresJugador = []
manoJugador = []
puntosJugador = 0
repartir(baraja, manoJugador, valoresJugador)
repartir(baraja, manoJugador, valoresJugador)
print(f"La mano del jugador es: {manoJugador}")
#print(valoresJugador)
print(f"Los puntos del jugador son: {puntosMano(valoresJugador , puntosJugador)}")

manoCrupier = []
valoresCrupier = []
manoCrupier = []
puntosCrupier = 0
repartir(baraja, manoCrupier, valoresCrupier)
repartir(baraja, manoCrupier, valoresCrupier)
print(f"La mano del crupier es: {manoCrupier}")
#print(valoresCrupier)
print(f"Los puntos del crupier son: {puntosMano(valoresCrupier , puntosCrupier)}")
   
