from random import *

def creer_liste_de_liste(hauteur,largeur):
    liste_alea=[]
    liste_de_liste=[]
    for j in range(4):
        for i in range(3):
            liste_alea.append(randint(0, 100))
        liste_de_liste.append(liste_alea)
        liste_alea=[]
    return(liste_de_liste)
mes_donnees=creer_liste_de_liste(4,3)
print(mes_donnees)