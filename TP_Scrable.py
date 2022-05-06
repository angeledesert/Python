#########################
##                     ##
##   TP DICTIONNAIRES  ##
##                     ##
#########################




#La fonction point() prend en paramètre une chaîne de caractère composée de lettres majuscules;


def points(mot):    #definiton de la fonction point
    score = 0   #au debut, le score est de 0
    liste_lettre = list(mot)
    scrabble={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10} #dictionnaire scrabble donne la valeur de chaque lettre de l'alphabet
    for lettre in liste_lettre : #pour chaque lettre du mot
        score += scrabble[lettre] #regarder la valeur de la lettre incrémenter la fonction score
    return score



print('######################')
print('##                  ##')
print('##      Scrabble    ##')
print("##                  ##")
print('######################')

continuer=1

while continuer==1:                                                             # Boucle permettant de relancer le programme
    mot_saisie=input("Pour calculer les points, entrer votre mot.")            # Demande une saisie clavier
    mot_saisie = mot_saisie.upper()                                             # Convertir le mot saisie en majuscule
    score = points(mot_saisie)                                                    # On utilise une fonction nommée points pour calculer le score.
    print (mot_saisie, "vaut", score, "points")                                        # On affiche le score
    continuer=int(input("Voulez vous calculer un autre mot ? [1-Oui/0-Non] :")) # Demande une saisie clavier