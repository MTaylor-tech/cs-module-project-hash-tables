IGNORE = ['"', ':', ';', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}',
          '(', ')', '*', '^', '&',',']

WHITESPACE = ['\r', '\n', '\t']

def word_count(s):
    s = s.lower()
    s = ''.join(c for c in s if c not in IGNORE)
    for c in WHITESPACE:
        s = s.replace(c," ")
    arr = s.split(" ")
    wordbank = {}
    for word in arr:
        if word == '':
            pass
        elif wordbank.get(word) is None:
            wordbank.update({word:1})
        else:
            count = wordbank.get(word)
            wordbank.update({word:count+1})
    return wordbank

def hist(filename):
    f = open(filename,"r")
    wb = word_count(f.read())
    swb = sorted(wb,key=lambda x: (-wb.get(x),x))
    count = 0
    for k in wb.keys():
        if len(k) > count:
            count = len(k)
    count += 2
    for w in swb:
        print(f"{w}{' '*(count-len(w))}{'#'*wb.get(w)}")
    f.close()

hist('robin.txt')
