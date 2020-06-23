color_grass = 'green'
count_of_cats = 28


def popis_stav():
    return 'Tráva je {barva}. Prohání se po ní {pocet} koťátek'.format(
        barva=color_grass, pocet=count_of_cats)
