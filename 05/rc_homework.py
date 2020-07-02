def get_num(rc):
    return int(''.join(x for x in rc if x.isdigit()))


def check_format(rc):
    if '/' not in rc or len(rc) != 11:
        raise Exception('Wrong format, length of number must be 11 and symbol / is expected.')
    if rc[6] != '/':
        raise Exception('Wrong position of char: /')
    rc = rc[:6] + rc[7:]
    for char in rc:
        if not char.isnumeric():
            raise Exception('Only numbers and / are expected.')


def check_dates(rc):
    if int(rc[2:4]) > 62 or int(rc[4:6]) > 31:
        raise Exception('Wrong date.')


def divisibility(rc):
    if get_num(rc) % 11 != 0:
        raise Exception('RC is not divisible by 11.')


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
    return "Date of birth: {}.{}.{}".format(day, month, year)


def get_sex(rc):
    if int(rc[2:4]) > 50:
        return 'Female'
    else:
        return 'Male'


if __name__ == "__main__":
    your_rc = input('Input your RC: ')
    try:
        check_format(your_rc)
        check_dates(your_rc)
        divisibility(your_rc)
    except ValueError:
        print('Wrong RC.')
    else:
        print(get_birthday(your_rc))
        print(get_sex(your_rc))
        print("RC is OK.")
