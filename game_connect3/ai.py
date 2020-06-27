import random
from utils import move


def move_pc(line, symbol):
    position = random.randint(0, len(line) - 1)
    if line[position] == '-':
        return move(line, position, symbol)
    elif not line.__contains__('-'):
        print("Game over. Draw.")
    else:
        return move_pc(line)
