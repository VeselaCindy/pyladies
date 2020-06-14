zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

chybne_zaznamy = []
spravne_zaznamy = []
opravene_zaznamy = []


for zaznam in zaznamy:
    rozdel = zaznam.split()
    if rozdel[0][0].islower() or rozdel[1][0].islower():
        chybne_zaznamy.append(zaznam)
        # oprava jmena
        oprava = rozdel[0].capitalize() + ' ' + rozdel[1].capitalize()
        opravene_zaznamy.append(oprava)
    else:
        spravne_zaznamy.append(zaznam)

print('Správné záznamy: ', spravne_zaznamy)
print('Chybné záznamy: ', chybne_zaznamy)
print('Opravené záznamy: ', opravene_zaznamy)

