import turtle
from itertools import cycle


turtle.pensize(3)
turtle.bgcolor("black")
turtle.speed("slow")
turtle.pencolor("yellow")
farg = cycle(["pink","red", "orange", "yellow", "green","cyan", "blue", "purple"])
bakgrund = cycle(["black", "white"])

def turtledraw (storlek, vinkel, vändning):
    turtle.circle(storlek)
    turtle.pencolor(next(farg))
    #turtle.bgcolor(next(bakgrund))
    turtle.right(vinkel)
    turtle.forward(vändning)
    turtledraw(storlek + 0, vinkel +8, vändning + 0)

turtledraw(30, 0, 1)