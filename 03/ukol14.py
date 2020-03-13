from turtle import forward, shape, exitonclick, left, right
from turtle import penup, pendown, setx, sety


shape("turtle")


for ctverec in range(18):
    for i in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()
