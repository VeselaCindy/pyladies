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
