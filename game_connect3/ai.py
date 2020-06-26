import random
from game_connect3.utils import move


def move_pc(line):
    position = random.randint(0, len(line) - 1)
    if line[position] == '-':
        return move(line, position, 'o')
    elif not line.__contains__('-'):
        print("Game over. Draw.")
    else:
        return move_pc(line)
