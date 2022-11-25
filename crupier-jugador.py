# Obtengo la mano del crupier.
manoCrupier = []
valoresCrupier = []
manoCrupier = []
puntosCrupier = 0

repartir(baraja, manoCrupier, valoresCrupier)
repartir(baraja, manoCrupier, valoresCrupier)
i = 0
while i == 0:
    print(f"La mano del crupier es: {manoCrupier}")
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
         
#blackJackCrupier = esBlackJack(puntosCrupier, manoCrupier)
print(f"Los puntos del crupier son: {(puntosCrupier)}")


# Obtengo la mano del jugador.
cartasJugador = []
valoresJugador = []
manoJugador = []
puntosJugador = 0
repartir(baraja, manoJugador, valoresJugador)
repartir(baraja, manoJugador, valoresJugador)
print(f"La mano del jugador es: {manoJugador}")
j = 0
while j == 0:
    for i in range(len(valoresJugador)): 
        if valoresJugador [i] == 1:   
            valoresJugador[i] = int(input(f"Elija qué valor le da al As. Las opciones son 1 y 11: "))
    print(manoJugador)
    print(f"Los puntos del jugador son: {puntosMano(valoresJugador , puntosJugador)}")
    z = 0
    while z == 0:
        decision = int(input(f"Ingrese 1 para detenerse, 2 para pedir otra carta: "))
        if decision == 1:
            j = 1
            z = 1
        elif decision == 2:
            repartir(baraja, manoJugador, valoresJugador)
            z = 1
