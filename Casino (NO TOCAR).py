import random
import time
desicion3=("")

##ARRAYS DEL TRAGAMONEDA
simbolos=["π","π","π","π","π","π"]

array1=["","","",""]
array2=["","","",""]
array3=["","","",""]

numerosnuma=[0]
#Ruleta europea
todos=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
impares=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
pares=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
negros=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
rojos=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]



print("BIENVENIDOS AL CASINO\n")

print("Escriba que juego desea jugar\n")
print("LAS OPCIONES SON")
print("ββββββββββββββββββββββββββββββ")
print("Ruleta") 
print("ββββββββββββββββββββββββββββββ")  
print("Tragamonedas")   
print("ββββββββββββββββββββββββββββββ")
print("Blackjack")
print("ββββββββββββββββββββββββββββββ")
print("Salir si desea retirarse.")
print("ββββββββββββββββββββββββββββββ")

desicion=str(input())
desicion=desicion.title()

while desicion==("Ruleta") or desicion==("Tragamonedas") or desicion==("Blackjack") and desicion!=("Salir"):
 
   if desicion==("Ruleta") and desicion!=("Salir"):
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("Usted eligiΓ³ el juego de la ruleta europea")
     time.sleep(1.5) 
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("Elija a que quiere apostar. Las opciones son:")
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("1) NΓΊmeros a elecciΓ³n")
     print("2) Par o Impar")
     print("3) Colores: Rojo o Negro")
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("Escriba 1, 2 o 3 dependiendo lo que quiera jugar")
     #aca se pone la variable dependiendo el juego a que se quiera jugar
     desicion2=int(input())
     
     while desicion2<=3:  #############################
      if desicion2==1:                            #RULETA OPCION 1
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         cantidadnuma=int(input("ΒΏCuΓ‘l es la cantidad de nΓΊmeros que desea seleccionar? Recuerde que es del 0 al 36\n"))
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         numerosnuma=[0]
         numerosnuma=numerosnuma*(cantidadnuma)
         print(numerosnuma)
         for i in range(len(numerosnuma)):
             print("Ingrese el nΓΊmero que desea jugar")
             numeropaso=int(input())
             numerosnuma[i]=numeropaso

         print("Sus nΓΊmeros seleccionados fueron",numerosnuma)
         randomruleta=random.choice(todos)
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomruleta)
         
         if randomruleta in numerosnuma:
            print("FELICIDADES, USTED GANΓ")
         else:
            print("USTED PERDIΓ")
         time.sleep(4)   
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("Elija a que quiere apostar. Las opciones son:")
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("1) NΓΊmeros a elecciΓ³n")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
      elif desicion2==2:                                ######## Pares o impares esta en un elif
         print("Usted eligiΓ³ la opciΓ³n de pares o impares")
         time.sleep(1)
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("ELIJA A LO QUE QUIERE APOSTAR:")
         print("1) PARES")
         print("2) IMPARES") 
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         desicion4=int(input())
         if desicion4==1:   
             print("USTED APOSTΓ A LOS PARES")                                 ### ELIJIO PARES
             randomPARES=random.choice(todos)
             if randomPARES in (pares):
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomPARES)
                 print("FELICIDADES, USTED GANΓ")
                 time.sleep(1.5)
             else:
                 print("El numero que salio en la ruleta fue el ",randomPARES)
                 print("USTED PERDIΓ")
                 time.sleep(1.5)
            #### COPIAR LO DEL DESICION 2 Y TODA LA COSA 
         elif desicion4==2: 
             print("USTED APOSTΓ A LOS IMPARES")                                 ## ELIJIO IMPARES
             randomIMPARES=random.choice(todos)
             if randomIMPARES in (impares):
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomIMPARES)
                 print("FELICIDADES, USTED GANΓ")
                 time.sleep(1.5)
             else:
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomIMPARES)
                 print("USTED PERDIΓ³")
                 time.sleep(1.5)
         
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("Elija a que quiere apostar. Las opciones son:")
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("1) NΓΊmeros a eleccion")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("βββββββββββββββββββββββββββββββββββββββββββββββ") 
      elif desicion2==3:
         print("Usted eligiΓ³ la opciΓ³n de Colores rojo o negro")
         time.sleep(1)
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("ELIJA A LO QUE QUIERE APOSTAR:")
         print("1) ROJO")
         print("2) NEGRO") 
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         desicioncolores=int(input())
         if  desicioncolores==1:   
             print("USTED APOSTΓ AL COLOR ROJO")                                 ### ELIJIO ROJO
             randomROJO=random.choice(todos)
             if randomROJO in (rojos):
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomROJO,"ROJO")
                 print("FELICIDADES, USTED GANΓ")
                 time.sleep(1.5)
             else:
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomROJO,"NEGRO")
                 print("USTED PERDIΓ")
                 time.sleep(1.5)
         elif  desicioncolores==2: 
             print("USTED APOSTΓ AL COLOR NEGRO")                                #ELIJIO NEGRO
             randomNEGRO=random.choice(todos)
             if randomNEGRO in (negros):
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomNEGRO)
                 print("FELICIDADES, USTED GANΓ")
                 time.sleep(1.5)
             else:
                 print("El nΓΊmero que saliΓ³ en la ruleta fue el ",randomNEGRO)
                 print("USTED PERDIΓ")
                 time.sleep(1.5)   

         time.sleep(2)   
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("Elija a que quiere apostar las opciones son:")
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")
         print("1) NΓΊmeros a elecciΓ³n")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("βββββββββββββββββββββββββββββββββββββββββββββββ")

     print("Escriba que juego desea jugar\n")
     print("LAS OPCIONES SON")
     print("ββββββββββββββββββββββββββββββ")
     print("Ruleta") 
     print("ββββββββββββββββββββββββββββββ")  
     print("Tragamonedas")   
     print("ββββββββββββββββββββββββββββββ")
     print("Blackjack")
     print("ββββββββββββββββββββββββββββββ")
     print("Salir si desea retirarse.")
     print("ββββββββββββββββββββββββββββββ")    
     desicion=str(input())
     desicion=desicion.title()
   elif desicion==("Tragamonedas") and desicion!=("Salir"):
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("Usted eligiΓ³ el juego del Tragamonedas")
     print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     print("Precione 1 para realizar una tirada")
     
     desiciontirada=int(input())      ###PRECIOCE UNA TECLA PARA TIRAR 

     

     if desiciontirada==1:
        for i in range(len(array1)):
         array1[i]=random.choice(simbolos)
         array2[i]=random.choice(simbolos)
         array3[i]=random.choice(simbolos)
         
     

     for i in range (len(array1)):
         print (array1[i],end=" ")
     print("")
     for i in range (len(array2)):
         print (array2[i],end=" ")
     print("") 
     for i in range (len(array3)):
         print (array3[i],end=" ") 
     print("") 
     
     #if array2[0]==array2[1] and array2==[2] and desiciontirada==1:
     """
     if array2[0]==array2[1] and array2[2]==array2[1] and array2[3]==array2[1]:
        print("FELICIDADES, USTED GANΓ")
     elif desiciontirada!=1:
        print("")  
     else:
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
        print("USTED PERDIΓ")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
    """    
     if array1[0]==array1[1] and array1[2]==array1[1] and array1[3]==array1[1] and desiciontirada==1:
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
        print("FELICIDADES USTED GANO EN LA FILA UNO")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     elif desiciontirada!=1:
        print("")  
     else:
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
        print("USTED PERDIO EN LA FILA UNO")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     if array2[0]==array2[1] and array2[2]==array2[1] and array1[3]==array1[1] and desiciontirada==1:
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
        print("FELICIDADES USTED GANO EN LA FILA DOS")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     elif desiciontirada!=1:
        print("")  
     else:
        
        print("USTED PERDIO EN LA FILA DOS")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     if array3[0]==array3[1] and array3[2]==array3[1] and array3[3]==array3[1] and desiciontirada==1:
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
        print("FELICIDADES USTED GANO EN LA FILA TRES")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")
     elif desiciontirada!=1:
        print("")  
     else:
        
        print("USTED PERDIO EN LA FILA TRES")
        print("βββββββββββββββββββββββββββββββββββββββββββββββ")


     
     time.sleep(2.5)
     print("Escriba que juego desea jugar\n")
     print("LAS OPCIONES SON")
     print("ββββββββββββββββββββββββββββββ")
     print("Ruleta") 
     print("ββββββββββββββββββββββββββββββ")  
     print("Tragamonedas")   
     print("ββββββββββββββββββββββββββββββ")
     print("Blackjack")
     print("ββββββββββββββββββββββββββββββ")
     print("Salir si desea retirarse.")
     print("ββββββββββββββββββββββββββββββ")    
     desicion=str(input())
     desicion=desicion.title()
    

   elif desicion == "Blackjack" and desicion != "Salir":
    print(f"\n")
    print("βββββββββββββββββββββββββββββββββββββββββββββββ")
    print("Usted eligiΓ³ el Blackjack")
    time.sleep(1.5) 
    print("βββββββββββββββββββββββββββββββββββββββββββββββ")
    print("BLACKJACK")
    print("βββββββββββββββββββββββββββββββββββββββββββββββ")
    # Para nuestro juego de Blackjack necesitamos importar el mΓ³dulo random de Python.
    import random

    def barajaNueva(numero):
        """Defino una funciΓ³n para crear una baraja nueva."""
        if numero == 1:
            picas = []
            corazones = []
            trebol = []
            diamante = []
            baraja = [picas, corazones, trebol, diamante]
            palos = [ "β " , "β₯", "β£", "β¦"]
            valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            for palo in palos:
                #print(palo)
                if palo == "β ":
                    for valor in valores:
                        valor += palo
                        picas.append(valor)
                elif palo == "β₯":
                    for valor in valores:
                        valor += palo
                        corazones.append(valor)
                elif palo == "β£":
                    for valor in valores:
                        valor += palo
                        trebol.append (valor)
                else:
                    for valor in valores:
                        valor += palo
                        diamante.append (valor)
        return baraja

    def repartir(baraja , mano, valor):
        """ Defino una funciΓ³n para repartir una carta al azar.
        
        Me devuelve una lista con la baraja actualizada, la carta, el valor numΓ©rico de la carta, la cantidad de Jotas y de Ases de mi mano. 
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
        """Defino una funciΓ³n para obtener el valor numΓ©rico de mi string carta."""
        valor = 0
        if carta[0] == "A":
            valor = 11
        elif carta [0] == "J" or carta[0] == "Q" or carta[0] == "K":
            valor = 10
        else:
            if len(carta) == 3:
                # Recorto mi cadena desde el Γ­ndice 0 al 1 inclusive.
                valor = int(carta[0:2:1])
            elif len(carta) == 2:
                valor = int(carta[0])
        return valor

    def puntosMano(valores, puntos):
        """Defino una funciΓ³n que calcule los puntos de mi mano."""
        for x in valores:
            puntos += x    
        return puntos

    def esBlackJack(puntos, mano):
        """Defino una funciΓ³n que evalΓΊa el puntaje para saber si es Black Jack."""
        blackJack = 0
        if puntos == 21 and len(mano) == 2:
            blackJack = 1
            return int(blackJack) 

    def nuevaPartida(k):
        """Defino una funciΓ³n para iniciar una nueva partida.
        
        k = 0 es el parΓ‘metro elegido para llamar la funciΓ³n."""
        while k == 0: 
            partida = int(input(f"Ingrese 1 para jugar otra vez o 2 para salir: "))
            if partida == 1:
                k = 1
            elif partida == 2:
                k = 1
            else:
                print(f"El valor {partida} ingresado no es vΓ‘lido.")
        return partida 
    
    # Cargo mis condiciones iniciales y doy condiciones para una nueva partida.
    partida = 1
    while partida == 1:
        otraPartida = 0
        partida = 0
        baraja = barajaNueva(1)

        # Obtengo la mano del crupier.
        valoresCrupier = []
        manoCrupier = []
        puntosCrupier = 0

        repartir(baraja, manoCrupier, valoresCrupier)
        repartir(baraja, manoCrupier, valoresCrupier)
        print(f"La mano del crupier es:")
        juegoCrupier = 0
        while juegoCrupier == 0:
            for x in manoCrupier:
                print( x, end=" ")
            print()        
            puntosCrupier = puntosMano(valoresCrupier , puntosCrupier)
            if puntosCrupier == 21:
                juegoCrupier = 1
            """Decido quΓ© valor toma el As del crupier en base a su puntaje.
    
                El As del crupier vale 1 sΓ³lo cuando se pasa de 21."""
            for j in range(len(valoresCrupier)):
                if valoresCrupier[j] == 11 and puntosCrupier > 21:
                    puntosCrupier -= 10
            """El crupier estΓ‘ obligado a tomar carta si su puntaje <= 16 y a detenerse si su puntaje >= 17."""
            if puntosCrupier >= 17:
                juegoCrupier = 1
            else:
                puntosCrupier = 0
                repartir(baraja, manoCrupier, valoresCrupier)    

        
        blackJackCrupier = esBlackJack(puntosCrupier, manoCrupier)
        print(f"Los puntos del crupier son: {(puntosCrupier)}\n")
        if puntosCrupier > 21:
            print(f"\n GANASTE!\n El crupier se pasΓ³ de 21\n")
            partida = nuevaPartida(otraPartida)
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
        juegoJugador = 0
        while juegoJugador == 0:
            for x in manoJugador:
                print(x, end = " ")
            print()
            for i in range(len(valoresJugador)): 
                if valoresJugador [i] == 11:   
                    valoresJugador[i] = int(input(f"Elija quΓ© valor le da al As. Las opciones son 1 y 11: "))
        
            puntosJugador = (puntosMano(valoresJugador , puntosJugador))
            print(f"Los puntos del jugador son: {puntosJugador}\n")
            z = 0
            while z == 0:
                decision = int(input(f"Ingrese 1 para pedir otra carta, 2 para detenerse: "))
                if decision == 2:
                    z = 1
                    juegoJugador = 1
                elif decision == 1:
                    puntosJugador = 0
                    repartir(baraja, manoJugador, valoresJugador)
                    z = 1
                else:
                    print("El valor ingresado no es vΓ‘lido.")
        blackJackJugador = esBlackJack(puntosJugador, manoJugador)
        if puntosJugador > 21:
            print(F"\n PERDISTE!\n  Te pasaste de 21\n")
            partida = nuevaPartida(otraPartida)
            if  partida == 1:
                continue
            elif partida == 2:
                break
        # Comparamos resultados si ninguno de los dos se pasΓ³ de 21.

        if puntosJugador == puntosCrupier and blackJackCrupier == blackJackJugador == 1:
            print(f"\n El jugador y el crupier EMPATAN!\n Ambos tienen BLACK JACK!")
            partida = nuevaPartida(otraPartida)
            if  partida == 1:
                continue
            elif partida == 2:
                break

        elif blackJackCrupier == 1 and blackJackJugador != 1:
            print(f"\n El crupier tiene \n BLACKJACK!\n PERDISTE!")
            partida = nuevaPartida(otraPartida)
            if  partida == 1:
                continue
            elif partida == 2:
                break
        elif blackJackJugador == 1 and blackJackCrupier != 1:
            print(f"\n El jugador tiene \n BLACKJACK!\n GANASTE!")
            partida = nuevaPartida(otraPartida)
            if  partida == 1:
                continue
            elif partida == 2:
                break
    
        elif blackJackCrupier == blackJackJugador != 1:
            if puntosCrupier == puntosJugador:
                print(f"\n EMPATAN!\n Ambos tienen {puntosCrupier} puntos.")
                partida = nuevaPartida(otraPartida)

            elif puntosJugador > puntosCrupier:
                print(f"\n GANASTE!\n")
                partida = nuevaPartida(otraPartida)
            elif puntosCrupier > puntosJugador:
                print(f"\n El crupier gana con {puntosCrupier} puntos.\n PERDISTE!")
                partida = nuevaPartida(otraPartida)
            else:
                print("ERROR")

            if  partida == 1:
                continue
            elif partida == 2:
                    break     
    time.sleep(2.5)
    print("Escriba que juego desea jugar\n")
    print("LAS OPCIONES SON")
    print("ββββββββββββββββββββββββββββββ")
    print("Ruleta") 
    print("ββββββββββββββββββββββββββββββ")  
    print("Tragamonedas")   
    print("ββββββββββββββββββββββββββββββ")
    print("Blackack")
    print("ββββββββββββββββββββββββββββββ")
    print("Salir si desea retirarse.")
    print("ββββββββββββββββββββββββββββββ")    
    desicion=str(input())
    desicion=desicion.title()