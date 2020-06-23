import random


# task 8
def roll_dice():
    return random.randint(1, 6)


def roll_until_six():
    count = 1
    while roll_dice() != 6:
        count += 1
    return count


def game():
    gamers = []
    for i in range(4):
        gamers.append(roll_until_six())
    print('Count of rolls: ', gamers)
    winner = gamers.index(max(gamers)) + 1
    print('Winner is gamer number', winner)


if __name__ == "__main__":
    game()
