speed = float(input("Zadejte rychlost Vaší chůze: "))
weight = int(input("Zadejte váhu ulovené ryby (v gramech): "))
antennae = int(input("Zadejte počet tykadel: "))
temp = float(input("Zadejte teplotu vody: "))
distance = float(input("Zadejte vzdálenost od rovníku: "))

if speed > 10:
    print("Jsi rychlý běžec.")
elif speed > 5:
    print("Jdete rychlou chůzí.")
elif speed >= 1:
    print("zrychli")
else:
    print("Nestůj!")

if weight > 1000:
    print("Asi to byl losos")
elif weight > 500:
    print("Dobrou chut")
elif weight > 100:
    print("nic moc")
else:
    print("Pust tu chudinku zpět!")

if antennae > 100:
    print("Tykadla všude")
elif antennae > 10:
    print("Máš se skvěle")
elif antennae > 1:
    print("pár ti jich zbylo")
else:
    print("Zajdi k doktorovi.")

if temp == 100:
    print("Voda vaří")
elif temp > 50:
    print("Pozor opaříš se")
elif temp > 20:
    print("voda je teplá, můžeš se jít koupat")
else:
    print("Přihřej si vodu.")    

if distance > 5000:
    print("Jsi asi na polu.")
elif distance > 1000:
    print("Mas se skvěle")
elif temp > 200:
    print("Super")
else:
    print("Jsi blizko rovníku. Asi ti je horko, co?")    
