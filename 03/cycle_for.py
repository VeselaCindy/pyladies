from turtle import forward, shape, exitonclick, left, right
from turtle import penup, pendown, setx, sety


for i in range(5):
    print(i)

soucet = 0
for c in 8,45, 9, 21:
    soucet = soucet + c

print(soucet)

shape("turtle")

"""
for i in range(4):
    forward(50)
    left(90)
"""

"""
for i in range(50):
    forward(i)
    penup()
    forward(5)
    pendown()

exitonclick()
"""



for ctverec in range(3):
    for i in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()
