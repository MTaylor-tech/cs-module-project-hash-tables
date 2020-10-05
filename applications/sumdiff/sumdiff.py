"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

xdict = {}
fdict = {}


def f(x):
    return x * 4 + 6


def fd(x):
    if fdict.get(x) is not None:
        return fdict.get(x)
    else:
        fx = f(x)
        fdict.update({x:fx})
        return fx


def num_order(x,y,reverse=False):
    if (x <= y and not reverse) or (y<=x and reverse):
        return (x,y)
    else:
        return (y,x)


def djb2(key):
    hash = 5381
    for char in key:
        hash = (( hash << 5) + hash) + ord(char)
    return hash & 0xFFFFFFFF


def ab_sum(a,b):
    hashd = djb2(f"{a}+{b}")
    if xdict.get(hashd) is not None:
        return xdict.get(hashd)
    else:
        answer = fd(a) + fd(b)
        xdict.update({hashd:answer})
        return answer


def cd_diff(c,d):
    hashd = djb2(f"{c}-{d}")
    if xdict.get(hashd) is not None:
        return xdict.get(hashd)
    else:
        answer = fd(c) - fd(d)
        xdict.update({hashd:answer})
        return answer


def check_same(a,b,c,d):
    (a,b) = num_order(a,b)
    ab = ab_sum(a,b)
    if ab == cd_diff(c,d):
        return ab
    else:
        return None


def sumdiff(q):
    for a in q:
        for b in q:
            for c in q:
                for d in q:
                    ch = check_same(a,b,c,d)
                    if ch is not None:
                        print(f"f({a}) + f({b}) = f({c}) - f({d})\t{fd(a)} + {fd(b)} = {fd(c)} - {fd(d)}\t{ch}")


def predict(q):
    for a in q:
        for b in q:
            ab_sum(a,b)
    for c in q:
        for d in q:
            cd_diff(c,d)

predict(q)
sumdiff(q)
