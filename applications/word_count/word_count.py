IGNORE = ['"', ':', ';', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}',
          '(', ')', '*', '^', '&',',']


def word_count(s):
    s = s.lower()
    s = ''.join(c for c in s if c not in IGNORE)
    arr = [w for w in s.split() if w!='']
    wordbank = {}
    for word in arr:
        count = wordbank.get(word)
        if count is None:
            wordbank.update({word:1})
        else:
            wordbank.update({word:count+1})
    return wordbank


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
