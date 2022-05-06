import os
import random as rd
nombreTire = rd.randint(0, 100)  #La fonction "randint" de la bibliothèque « random » tire un nombre entier
print ("\t\t    === JEU DU C'EST PLUS, C'EST MOI?S ===\n\n")

nombreTape = 0

while nombreTape != nombreTire :
      nombreTape = int(input("Tapez un nombre entier entre 0 et 100 :"))
      if nombreTape > nombreTire :
            print("c'est moins\n\n")

      elif nombreTape < nombreTire:
            print("c'est plus\n\n")

      else :
            print("c'est gagné")