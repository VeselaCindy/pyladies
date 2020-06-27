from utils import move
from ai import move_pc


def evaluate(line, user_symbol='x', pc_symbol='o'):
    print("Current state:", line)
    if ('xxx' in line and user_symbol == 'x') or ('ooo' in line and user_symbol == 'o'):
        print('You are a winner! Congratulation.')
        return 'x'
    elif ('ooo' in line and pc_symbol == 'o') or ('xxx' in line and pc_symbol == 'x'):
        print('You are lost.')
        return 'o'
    elif '-' not in line:
        print('Draw')
        return '!'
    else:
        return '-'


def move_gamer(line, symbol):
    while True:
        try:
            position = int(input('Input position: ')) - 1
            if position < len(line) and line[position] == '-':
                return move(line, position, symbol)
            else:
                print('Wrong position, input it again, please...')
        except ValueError:
            print('Input value, please.. try again..')


def choose_symbol():
    user_symbol = input('Input your symbol x or o.')
    while user_symbol != 'o' and user_symbol != 'x':
        print('Wrong symbol. Try it again.')
        user_symbol = input('Input your symbol x or o.')
    return user_symbol


def connect_1d():
    line = 19 * '-'
    user_symbol = choose_symbol()
    if user_symbol == 'o':
        pc_symbol = 'x'
    else:
        pc_symbol = 'o'
    while evaluate(line, user_symbol, pc_symbol) == '-':
        line = move_gamer(line, symbol=user_symbol)
        line = move_pc(line, symbol=pc_symbol)


if __name__ == "__main__":
    connect_1d()
