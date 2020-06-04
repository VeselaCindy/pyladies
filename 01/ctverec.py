a = float(input("Zadej velikost strany čtverce: "))
cislo_spravne = a > 0

if cislo_spravne:
    o = 4 * a
    S = a**2
    print('Obvod čtverce se stranou ' + str(a) + ' cm je ' + str(o) +  ' cm.')
    print('Obsah čvterce se stranou ' + str(a) + ' cm je ' + str(S) +' cm2.')
else:
    print('Zadejte stranu kladnou stranu čtverce.')

print("Díky za použití kalkulačky.")



