from turtle import shape, speed, forward, left, right, exitonclick, setx

shape('turtle')
speed(10)
delka = 1
uhel = 180 - (180*(1-2/95))

for i in range(2000):
    forward(delka/95)
    left(uhel)
    delka = delka + 0.5

exitonclick()