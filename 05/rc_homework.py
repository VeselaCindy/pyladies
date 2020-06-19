def get_num(rc):
    return int(''.join(x for x in rc if x.isdigit()))


def check_format(rc):
    if '/' not in rc or len(rc) != 11:
        return Exception('Wrong format. The length must be 11.')
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
    if int(rc[2:4]) > 62 or int(rc[4:6]) > 31:
        print('Wrong date.')
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
    year_rc = rc[0:2]
    if int(year_rc) < 54:
        year = int('20' + year_rc)
    else:
        year = int('19' + year_rc)
    month = int(rc[2:4])
    if month > 50:
        month -= 50
    day = int(rc[4:6])
    print("Date of birth: {}.{}.{}".format(day, month, year))
    return day, month, year


def get_sex(rc):
    if int(rc[2:4]) > 50:
        return 'Female'
    else:
        return 'Male'


def check_rc():
    rc = input('Input your RC: ')
    if not check_format(rc) or not check_dates(rc) or not divisibility(rc):
        return False
    else:
        get_birthday(rc)
        print(get_sex(rc))
        return True


check_rc()
