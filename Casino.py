import random
import time
desicion3=("")

##ARRAYS DEL TRAGAMONEDA
simbolos=["🍋","🍒","🍇","🍉","🍀","💎"]

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
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Ruleta") 
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")  
print("Tragamonedas")   
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Black Jack")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

desicion=str(input())
desicion=desicion.title()

while desicion==("Ruleta") or desicion==("Tragamonedas") or desicion==("Black Jack") and desicion!=("salir"):
 
   if desicion==("Ruleta") and desicion!=("Salir"):
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Usted elijio el juego de la ruleta europea")
     time.sleep(1.5) 
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Elija a que quiere apostar las opciones son:")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("1) Numeros a eleccion")
     print("2) Par o Impar")
     print("3) Colores: Rojo o Negro")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Escriba 1 2 o 3 dependiendo lo que quiera jugar")
     #aca se pone la variable dependiendo el juego a que se quiera jugar
     desicion2=int(input())
     
     while desicion2<=3:  #############################
      if desicion2==1:                            #RULETA OPCION 1
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         cantidadnuma=int(input("cual es la cantidad de numeros que desea seleccionar recuerde que es del 0 al 36\n"))
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         numerosnuma=[0]
         numerosnuma=numerosnuma*(cantidadnuma)
         print(numerosnuma)
         for i in range(len(numerosnuma)):
             print("ingrese el numero que desea jugar")
             numeropaso=int(input())
             numerosnuma[i]=numeropaso

         print("sus numeros seleccionados fueron",numerosnuma)
         randomruleta=random.choice(todos)
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("El numero que salio en la ruleta fue el ",randomruleta)
         
         if randomruleta in numerosnuma:
            print("FELICIDADES GANO")
         else:
            print("USTED PERDIO")
         time.sleep(4)   
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("Elija a que quiere apostar las opciones son:")
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("1) Numeros a eleccion")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
      elif desicion2==2:                                ######## Pares o impares esta en un elif
         print("Usted elijio la opcion de pares o impares")
         time.sleep(1)
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("ELIJA A LO QUE QUIERE APOSTAR:")
         print("1) PARES")
         print("2) IMPARES") 
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         desicion4=int(input())
         if desicion4==1:   
             print("USTED APOSTO A LOS PARES")                                 ### ELIJIO PARES
             randomPARES=random.choice(todos)
             if randomPARES in (pares):
                 print("El numero que salio en la ruleta fue el ",randomPARES)
                 print("FELICIDADES USTED GANO")
                 time.sleep(1.5)
             else:
                 print("El numero que salio en la ruleta fue el ",randomPARES)
                 print("USTED PERDIO")
                 time.sleep(1.5)
            #### COPIAR LO DEL DESICION 2 Y TODA LA COSA 
         elif desicion4==2: 
             print("USTED APOSTO A LOS IMPARES")                                 ## ELIJIO IMPARES
             randomIMPARES=random.choice(todos)
             if randomIMPARES in (impares):
                 print("El numero que salio en la ruleta fue el ",randomIMPARES)
                 print("FELICIDADES USTED GANO")
                 time.sleep(1.5)
             else:
                 print("El numero que salio en la ruleta fue el ",randomIMPARES)
                 print("USTED PERDIO")
                 time.sleep(1.5)
         
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("Elija a que quiere apostar las opciones son:")
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("1) Numeros a eleccion")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
      elif desicion2==3:
         print("Usted elijio la opcion de Colores rojo o negro")
         time.sleep(1)
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("ELIJA A LO QUE QUIERE APOSTAR:")
         print("1) ROJO")
         print("2) NEGRO") 
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         desicioncolores=int(input())
         if  desicioncolores==1:   
             print("USTED APOSTO AL COLOR ROJO")                                 ### ELIJIO ROJO
             randomROJO=random.choice(todos)
             if randomROJO in (rojos):
                 print("El numero que salio en la ruleta fue el ",randomROJO,"ROJO")
                 print("FELICIDADES USTED GANO")
                 time.sleep(1.5)
             else:
                 print("El numero que salio en la ruleta fue el ",randomROJO,"NEGRO")
                 print("USTED PERDIO")
                 time.sleep(1.5)
         elif  desicioncolores==2: 
             print("USTED APOSTO AL COLOR NEGRO")                                #ELIJIO NEGRO
             randomNEGRO=random.choice(todos)
             if randomNEGRO in (negros):
                 print("El numero que salio en la ruleta fue el ",randomNEGRO)
                 print("FELICIDADES USTED GANO")
                 time.sleep(1.5)
             else:
                 print("El numero que salio en la ruleta fue el ",randomNEGRO)
                 print("USTED PERDIO")
                 time.sleep(1.5)   

         time.sleep(2)   
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("Elija a que quiere apostar las opciones son:")
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
         print("1) Numeros a eleccion")
         print("2) Par o Impar")
         print("3) Colores: Rojo o Negro")
         print("Escriba 4 si desea salir")  
         desicion2=int(input())     
         print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

     print("Escriba que juego desea jugar\n")
     print("LAS OPCIONES SON")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Ruleta") 
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")  
     print("Tragamonedas")   
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Black Jack")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")    
     desicion=str(input())
     desicion=desicion.title()
   elif desicion==("Tragamonedas") and desicion!=("Salir"):
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Usted elijio el juego del Tragamonedas")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
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
     
     if array2[0]==array2[1] and array2==[2] and desiciontirada==1:
        print("FELICIDADES USTED GANO")
     elif desiciontirada!=1:
        print("")  
     else:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("USTED PERDIO")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
     


     
     time.sleep(2.5)
     print("Escriba que juego desea jugar\n")
     print("LAS OPCIONES SON")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Ruleta") 
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")  
     print("Tragamonedas")   
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
     print("Black Jack")
     print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")    
     desicion=str(input())
     desicion=desicion.title()