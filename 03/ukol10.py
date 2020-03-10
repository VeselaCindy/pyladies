from turtle import shape, speed, forward, left, right, exitonclick, setx

shape('turtle')
delka = 10
for i in range(19):
    left(90)
    forward(delka)
    delka = delka + 5