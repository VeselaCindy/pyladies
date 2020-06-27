def move(line, position, symbol):
    line = list(line)
    if 0 <= position < len(line) or (position <= 0 and abs(position) <= len(line)):
        line[position] = symbol
        return ''.join(line)
    else:
        raise IndexError('Position {n} is out of range!'.format(n=position))
