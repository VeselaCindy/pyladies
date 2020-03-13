first = int(input("Zadej první číslo: "))
second = int(input("Zadej druhé číslo: "))
oper = input("Zadej operaci: ")

if oper == "+":
    result = first + second
elif oper == "-":
    result = first - second
elif oper == "/":
    if second != 0:
        result = first/second
    else:
        print("Nelze spočítat!")
        result = None
elif oper == "*":
    result = first*second
else:
    print("neplatná operace")
    result = None

print(first, oper, second, "=", result)