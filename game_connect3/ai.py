import random
from utils import move


def move_pc(line, symbol):
    if len(line) == 0:
        raise ValueError('Line must be longer than 0.')
    else:
        position = random.randint(0, len(line) - 1)
        if line[position] == '-':
            return move(line, position, symbol)
        elif not line.__contains__('-'):
            print('Game over')
            return 'Game over'
        else:
            return move_pc(line, symbol)
