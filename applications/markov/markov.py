import random

WHITESPACE = ['\r', '\n', '\t']
FILENAME = "input.txt"

def word_grab(s):
    for c in WHITESPACE:
        s = s.replace(c," ")
    arr = s.split(" ")
    wordbank = {}
    i = 0
    for i in range(len(arr)-1):
        if arr[i] == '':
            pass
        elif wordbank.get(arr[i]) is None:
            wordbank.update({arr[i]:[arr[i+1]]})
        else:
            current = wordbank.get(arr[i])
            if arr[i+1] != '' and arr[i+1] not in current:
                current.append(arr[i+1])
                wordbank.update({arr[i]:current})
    return wordbank

# Read in all the words in one go
def markov(filename,length=100):
    with open(filename,"r") as f:
        words = f.read()
        w = word_grab(words)
        l = list(w.keys())
        for k in l:
            if k == '' or w.get(k) is None or w.get(k)=='':
                l.remove(k)
        t = None
        while t is None:
            t = [random.choice(l)]
        # print(t)
        # print(w.get(t[0]))
        while len(t) <= length:
            wc = w.get(t[-1])
            # while wc == '' or wc is None:
            #     wc = w.get(random.choice(l))
            if wc is not None:
                t.append(random.choice(wc))
            else:
                t.remove(t[-1])
                # t.append(random.choice(w.get(t[-1])))
        s = ' '.join(t)
        return s



# TODO: construct 5 random sentences
# Your code here
print(markov(FILENAME))
