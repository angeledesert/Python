# Créé par deserta, le 04/10/2021 en Python 3.7
import turtle as t

def courbe(n,cote):
    if n==0:
        t.forward(cote)
    else:
        courbe(n-1,cote/3)
        t.left(60)
        courbe(n-1,cote/3)
        t.right(120)
        courbe(n-1,cote/3)
        t.left(60)
        courbe(n-1,cote/3)

def flocon(n,long):
    t.left(60)
    courbe(n,long)
    t.right(120)
    courbe(n,long)
    t.right(120)
    courbe(n,long)

t.penup()
t.goto(-100, 0)
t.pendown()
# orientation intiale de la tête :
#vers la droite de l’écran
t.setheading(0)
t.hideturtle() # on cache la tortue
t.speed(0) # on accélère la tortue
t.color("purple")
t.pensize(3)

flocon(3,200)

t.exitonclick()