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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
