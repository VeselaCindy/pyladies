from turtle import shape, speed, forward, left, right, exitonclick, setx

shape('turtle')
delka = 2
for i in range(38):
    left(60)
    forward(delka)
    delka = delka + 2

exitonclick()