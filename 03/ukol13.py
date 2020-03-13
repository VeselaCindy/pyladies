from turtle import *
import random


shape('turtle')
bgcolor("black")
pencolor("yellow")
speed(10)
penup()
setx(-300)
pendown()

for star in range(5):
    delka = random.randrange(50,200)
    #fillcolor("yellow")
    #begin_fill()
    for i in range(5):
        forward(delka)
        right(144)
    #end_fill()
    penup()
    forward(delka + random.randrange(10,50))
    pendown()


for star in range(5):
    delka = random.randrange(50,200)
    fillcolor("yellow")
    begin_fill()
    for i in range(5):
        forward(delka)
        right(144)
    end_fill()
    penup()
    forward(delka + random.randrange(10,50))
    pendown()

exitonclick()