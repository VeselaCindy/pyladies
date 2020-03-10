from turtle import shape, speed, forward, left, right, exitonclick, setx

pocet_stran = 95
uhel = 180 - (180*(1-2/pocet_stran))

for i in range(pocet_stran):
    forward(200/pocet_stran)
    left(uhel)

exitonclick()
