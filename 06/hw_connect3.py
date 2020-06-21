def evaluate(line):
    if 'xxx' in line:
        return 'x'
    elif 'ooo' in line:
        return 'o'
    elif '-' not in line:
        return '!'
    else:
        return '-'


print(evaluate('oxooxxoxx'))


def move(line, position, symbol):
    line = list(line)
    line[position] = symbol
    return ''.join(line)


def move_gamer(line):
    while True:
        try:
            position = int(input('Input position: ')) - 1
            if position < len(line) and line[position] == '-':
                while True:
                    symbol = input('Symbol: ')
                    if symbol == 'o' or symbol == 'x':
                        return move(line, position, symbol)
                    else:
                        print('Wrong symbol, input x or o, please...')
            else:
                print('Wrong position, input it again, please...')
        except ValueError:
            print('Input value, please.. try again..')


print(move_gamer('xxxx-'))
