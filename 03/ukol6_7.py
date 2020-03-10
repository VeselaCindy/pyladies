# pokud zadam v inputu 5, 6, 7, 8 - ziskam ukol čislo 6
# obecne (ukol 7):
from turtle import shape, speed, forward, left, right, exitonclick, setx

pocet_stran = int(input("Zadej počet stran: "))
uhel = 180 - (180*(1-2/pocet_stran))

for i in range(pocet_stran):
    forward(200/pocet_stran)
    left(uhel)

exitonclick()