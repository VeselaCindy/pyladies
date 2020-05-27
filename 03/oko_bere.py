import random 

body = 0

while(True):
    print('Počet bodů: ',body)
    cont = input('Chceš pokračovat? ')
    if cont == 'ne':
        print('Hra skončila. Počet bodů: ', body)
        break
    elif cont == 'ano':
        pricti = random.randrange(2,10)
        print('Aktuální hodnota karty: ', pricti)
        body = body + pricti
        if body > 21:
            print('Hra skončila. Počet bodů: ', body)
            break
    else:
        print('špatný vstup')