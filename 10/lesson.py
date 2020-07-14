import time


def time_it(fn):
    def inner(*args):
        start = time.time()
        result = fn(*args)
        print('Function call took {} seconds.'.format(time.time() - start))
        return result

    return inner


@time_it
def do_something():
    i = 0
    while i < 10000000:
        i += 1


do_something()
