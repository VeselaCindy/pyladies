from game_connect3.utils import move
from game_connect3.ai import move_pc


def evaluate(line):
    print("Current state:", line)
    if 'xxx' in line:
        print('You are a winner! Congratulation.')
        return 'x'
    elif 'ooo' in line:
        print('You are lost.')
        return 'o'
    elif '-' not in line:
        print('Draw')
        return '!'
    else:
        return '-'


def move_gamer(line):
    symbol = 'x'
    while True:
        try:
            position = int(input('Input position: ')) - 1
            if position < len(line) and line[position] == '-':
                return move(line, position, symbol)
            else:
                print('Wrong position, input it again, please...')
        except ValueError:
            print('Input value, please.. try again..')


def connect_1d():
    line = 19 * '-'
    while evaluate(line) == '-':
        line = move_gamer(line)
        line = move_pc(line)


if __name__ == "__main__":
    connect_1d()
