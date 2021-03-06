from datetime import datetime


def get_num(rc):
    try:
        return int(''.join(x for x in rc if x.isdigit()))
    except ValueError:
        print('No numbers in the argument.')
        return None


def check_format(rc):
    if '/' not in rc or len(rc) != 11:
        return False
    if rc[6] != '/':
        print('Wrong position of char: /')
        return False
    rc = rc[:6] + rc[7:]
    for char in rc:
        if not char.isnumeric():
            print('Only numbers are expected.')
            return False
    return True


def check_dates(rc):
    date = rc[:6]
    if int(date[2]) >= 5:
        date = list(date)
        date[2] = str(int(date[2]) - 5)
        date = ''.join(date)
    try:
        datetime.strptime(date, '%y%m%d')
    except ValueError:
        print('Wrong dateformat')
        return False
    else:
        return True


def divisibility(rc):
    if get_num(rc) % 11 == 0:
        return True
    else:
        print('RC is not divisible by 11.')
        return False


def get_birthday(rc):
    year_rc = int(rc[0:2])
    if year_rc < 54:
        year = 2000 + year_rc
    else:
        year = 1900 + year_rc
    month = int(rc[2:4])
    if month > 50:
        month -= 50
    day = int(rc[4:6])
    return 'Date of birth: {}.{}.{}'.format(day, month, year)


def get_sex(rc):
    if int(rc[2:4]) > 50:
        return 'Female'
    else:
        return 'Male'


if __name__ == "__main__":
    your_rc = input('Input your RC: ')
    if check_format(your_rc) and check_dates(your_rc) and divisibility(your_rc):
        print(get_birthday(your_rc))
        print(get_sex(your_rc))
        print("RC is OK.")
    else:
        print("Wrong RC.")
