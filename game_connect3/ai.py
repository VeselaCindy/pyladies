import random
from utils import move


def put_symbol_next_to_substring(line, substring):
    xx_positions = [i for i in range(len(line)) if line.startswith(substring, i)]
    for possibility in xx_positions:
        if possibility > 0 and line[possibility - 1] == '-':
            return possibility - 1
        elif possibility < len(line) - len(substring) and line[possibility + len(substring)] == '-':
            return possibility + len(substring)
    return None


def random_move(line, symbol):
    if '---' in line:
        position = line.index('---') + 1
        return move(line, position, symbol)
    else:
        position = random.randint(0, len(line) - 1)
        if line[position] == '-':
            return move(line, position, symbol)
        else:
            return move_pc(line, symbol)


def move_pc(line, symbol):
    if len(line) == 0:
        raise ValueError('Line must be longer than 0.')
    else:
        if '-' not in line:
            print('Game over')
            return 'Game over'
        elif symbol not in line:
            return random_move(line, symbol)
        elif symbol * 2 in line:
            position = put_symbol_next_to_substring(line, substring=symbol * 2)
            if position is None:
                position = put_symbol_next_to_substring(line, substring=symbol)
        else:
            position = put_symbol_next_to_substring(line, substring=symbol)
    if position is not None:
        return move(line, position, symbol)
    else:
        return random_move(line, symbol)
