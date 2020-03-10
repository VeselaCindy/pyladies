from turtle import shape, forward, left, right

# 0: celá čísla v rozsahu podle vloženého argumentu 
# 1: celá čásla v intervalu od, do, viz for cyklus

for i in range(2,5):
    print(i)

# 2: čísla v intervalu s krokem - viz příklad <0,10) v krokem 2
for i in range(0,10,2):
    print(i)

# 3: 
shape("turtle")
forward(50)
left(120)
forward(50)
left(120)
forward(50)

exitonclick()

