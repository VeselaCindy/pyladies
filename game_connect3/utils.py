def move(line, position, symbol):
    line = list(line)
    line[position] = symbol
    return ''.join(line)