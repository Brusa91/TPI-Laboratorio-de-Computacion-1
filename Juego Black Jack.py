# Brusadin Leonardo Andrés.
# Legajo 15535.

# Para nuestro juego de Black Jack necesitamos importar el módulo random de Python.
import random

# Defino una función para crear una baraja nueva.
def barajaNueva(numero):
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

# Defino una función para repartir una carta al azar.
def repartir(baraja , mano):
    # Selecciono una carta al azar.
    palo = random.choice(baraja)
    carta =str(random.choice(palo))
    mano.append(carta)
    # Elimino la carta de las disponibles en la baraja.
    palo.remove(carta)
    return baraja , mano

baraja = barajaNueva(1)
mano = []
repartir(baraja, mano)

#print(mano)
#print(baraja)
