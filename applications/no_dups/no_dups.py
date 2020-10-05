def no_dups(s):
    # a = set(s.split()) #removes order
    a = s.split()
    d = {}
    b = []
    for w in a:
        if not d.get(w):
            d[w] = True
            b.append(w)
    return " ".join(b)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
