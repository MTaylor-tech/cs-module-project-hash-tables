table = {}

def djb2(key):
    """
    DJB2 hash, 32-bit

    Implement this, and/or FNV-1.
    """
    hash = 5381
    for char in key:
        hash = (( hash << 5) + hash) + ord(char)
    return hash & 0xFFFFFFFF


def expensive_seq(x, y, z):
    if x <= 0:
        return y + z
    if x >  0:
        hashd = djb2(f"{x},{y},{z}")
        if table.get(hashd) is not None:
            return table.get(hashd)
        else:
            answer = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
            table.update({hashd:answer})
            return answer



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
