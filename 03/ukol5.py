from turtle import shape, speed, forward, left, right, exitonclick, setx

# 5:
shape("turtle")
speed(10)
penup()
setx(-300)
pendown()

for i in range(10):
    left(45)
    forward(84.5)
    right(225)
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    left(135)
    forward(84.5)
    right(90)
    forward(42.5)
    right(90)
    forward(42.5)
    right(45)
    forward(60)
    left(90)
    forward(20)

exitonclick()