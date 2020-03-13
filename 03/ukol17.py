from math import inf

result = inf

for i in range(5):
    current = int(input("Zadej číslo: "))
    if current < result:
        result = current

print("Nejmenší zadané číslo je:", result)

