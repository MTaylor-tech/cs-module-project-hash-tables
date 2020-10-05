import random
import math


facd = {}
divd = {}
modd = {}
fd = {}


def djb2(key):
    hash = 5381
    for char in key:
        hash = (( hash << 5) + hash) + ord(char)
    return hash & 0xFFFFFFFF


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = 0
    hashd = djb2(f"{x},{y}")
    if fd.get(hashd) is not None:
        return fd.get(hashd)
    else:
        v = math.pow(x,y)
    if facd.get(v) is not None:
        v = facd.get(v)
    else:
        z = v
        v = math.factorial(v)
        facd.update({z:v})
    if divd.get(hashd) is not None:
        v = divd.get(hashd)
    else:
        v //= (x+y)
        divd.update({hashd:v})
    if modd.get(v) is not None:
        v = modd.get(v)
    else:
        z = v
        v %= 982451653
        modd.update({z:v})
        fd.update({hashd:v})
    return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
