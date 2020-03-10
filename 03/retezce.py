"""
jmeno = input("Zadej jméno: ")
prijmeni = input("zadej přijímení: ")

print('Tvé iniciály jsou:', jmeno[0].upper()+prijmeni[0].upper())

# formatovani
vypis = '{prvni}x{druhe} je {vysl}'.format(druhe =3,prvni=4, vysl=3*4)
print(vypis)
"""

retezec = input("Zadej slovo: ")
index = int(input("Zadej místo, kde chceš znat vyměnit: "))
co = input("Zadej písmeno, které chceš na toto místo: ")

if len(retezec) < index:
    print("Nelze")
else:
    prvni_cast = retezec[:index] 
    druha_cast = retezec[index+1:]
    novy_retezec =   prvni_cast + co + druha_cast
    print(novy_retezec)