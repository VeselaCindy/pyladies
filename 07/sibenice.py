import random
from sibenice_outputs import image, count

list_of_words = ['dog', 'friend', 'cream', 'chocolate', 'success']


def change_symbol(text, position, symbol):
    text = list(text)
    text[position] = symbol
    return ''.join(text)


def move(word, current):
    char = input('Input character: ')
    if len(char) > 0 and char in word:
        positions = [i for i in range(len(word)) if word.startswith(char, i)]
        for i in positions:
            if word.startswith(char, i):
                current = change_symbol(current, i, char)
        return current, True
    else:
        return current, False


if __name__ == '__main__':
    word = random.choice(list_of_words)
    current_state = '_' * len(word)
    count_of_failure = 0

    while '_' in current_state:
        current_state, success = move(word, current_state)
        if not success:
            count_of_failure += 1
            print(image(count_of_failure - 1))
            if count_of_failure >= count():
                print('Game over.')
                break
        print(current_state)
    if current_state == word:
        print('Congratulation.')
