# 0
zvirata = ['pes', 'kocka', 'andulka', 'králík', 'had', 'pav']


# 1
def print_names_less_5_letter(seznam):
    for i in seznam:
        if len(i) < 5:
            print(i)


print_names_less_5_letter(zvirata)


# 2
def print_names_start_with_k(seznam):
    for i in seznam:
        if i[0] == 'k':
            print(i)


# 3

def word_in_list(slovo, seznam):
    print(slovo in seznam)


word_in_list('pes', zvirata)


# 4
def make_lists(list1, list2):
    sjednoceni = list1
    prunik = []
    prvni = []
    druhy = []
    for i in list1:
        if i not in list2:
            prvni.append(i)

    for i in list2:
        if i not in list1:
            druhy.append(i)

    for i in list1:
        if i in list2:
            prunik.append(i)
    for i in list2:
        if i not in sjednoceni:
            sjednoceni.append(i)

    print('pouze v prvnim: ', prvni)
    print('pouze v druhem: ', druhy)
    print('vse: ', sjednoceni)
    print('v obou', prunik)
    return prvni, druhy, sjednoceni


make_lists(['jedna', 'dva', 'tri'], ['jedna', 'ahoj'])


# 5

def sort_animals(list1):
    serad = sorted(list1)
    print(serad)


# sort_animals(zvirata)

# 6
def sort_accord_second_letter(list1):
    podle_klice = dict([])
    for zvire in list1:
        klic = zvire[1]
        podle_klice.update({klic: zvire})

    seradene = []
    for key, value in sorted(podle_klice.items()):
        seradene.append(value)
    print(seradene)
    return seradene


# sort_accord_second_letter(zvirata)

# 7
# rodne cislo
def check_rc():
    rc = input('Zadej rodne cislo: ')
    if '/' not in rc or len(rc) != 11:
        raise Exception("Wrong format")
    else:
        # rodne_cislo = rodne_cislo.split('/')
        print('ok')

    cislo = ''
    for i, char in enumerate(rc):
        if i == 6:
            if char != '/':
                return False
        else:
            if not char.isnumeric():
                return False
            cislo += char

    if int(cislo) % 11 == 0:
        print('Rodne cislo je platne.')
        return True
    else:
        return False


check_rc()
