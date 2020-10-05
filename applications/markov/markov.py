import random

FILENAME = "input.txt"
ENDP = ['.','!','?']


def word_grab(s):
    arr = [w for w in s.split() if w!='']
    wordbank = {}
    prev_word = None
    for word in arr:
        if prev_word is None:
            prev_word = word
        else:
            next_words = wordbank.get(prev_word)
            if next_words is None:
                wordbank.update({prev_word:[word]})
            else:
                wordbank.update({prev_word:next_words+[word]})
            prev_word = word
    print(f"Analysis done. {len(arr)} words.")
    return wordbank


def check_word(word):
    start_quote = False
    end_quote = False
    end_word = False
    if word[0] == '"':
        start_quote = True
    if word[-1] == '"':
        end_quote = True
    if word[-1] in ENDP:
        end_word = True
    elif end_quote and word[-2] in ENDP:
        end_word = True
    return (start_quote,end_quote,end_word)


def cap_word(word,start_quote=False):
    if start_quote:
        word = word[:2].upper() + word[2:]
    else:
        word = word.capitalize()
    return word


def markov(filename,num_sentences=0,word_limit=0):
    with open(filename,"r") as f:
        words = f.read()
        wordbank = word_grab(words)
        wordlist = [w for w in wordbank.keys() if len(wordbank.get(w))>0]
        text = []
        while len(text) < 1:
            begin_word = (random.choice(wordlist))
            if begin_word is not None and begin_word != '':
                text.append(begin_word)
        current_word = text[0]
        (start_quote,end_quote,end_word) = check_word(text[0])
        at_beginning = end_word
        in_quote = start_quote
        text[0] = '\n\t' + cap_word(text[0],start_quote)
        sentence_count = 0
        word_count = 0
        print(f"Starting word: \'{current_word}\'")
        limit = 0
        limit_type = 0
        n = 0
        x = 0
        worry_limit = 10000
        if num_sentences > 0:
            limit = num_sentences
        elif word_limit > 0:
            limit = word_limit
            limit_type = 1
            if word_limit > worry_limit:
                worry_limit = word_limit + 1000
        else:
            limit = 10
        next_word = None
        while n <= limit and x <= worry_limit:
            word_options = wordbank.get(current_word)
            if len(word_options) == 1:
                next_word = word_options[0]
            else:
                next_word = random.choice(word_options)
            if wordbank.get(next_word) is None:
                pass
            else:
                (start_quote,end_quote,end_word) = check_word(next_word)
                if end_quote and not in_quote:
                    continue
                w = next_word
                if start_quote and not in_quote:
                    in_quote = True
                elif in_quote and end_quote:
                    in_quote = False
                if at_beginning:
                    w = cap_word(w,start_quote)
                text.append(w)
                current_word = next_word
                word_count += 1
                if limit_type == 1:
                    n += 1
                if end_word:
                    at_beginning = True
                    sentence_count += 1
                    if limit_type == 0:
                        n += 1
                    if sentence_count % 5 == 0:
                        text.append('\n\t')
                else:
                    at_beginning = False
            x += 1
        s = ' '.join(text)
        print(s)
        print(f"\nComplete. {sentence_count} sentences. {word_count} words.")
        return s

markov(FILENAME)
        # Dear, let's pretend we're kings and Alice picked up the glass, and down the ball, as if I feel somehow as far better manners! You ought, Dinah, you know, I can't deny it, somehow, Kitty. Let's pretend the Red Queen said, 'if you hear the shovel--and here I can tell, you like our passage in disgrace. "Really, Dinah washed her hands and down the arm-chair, half asleep, the King went on, "I assure, you don't make me through the Looking-glass) had really I turned over the King, so tidy as the great arm-chair, taking the ashes, "Mind the air had to prison, I do so wish it hadn't been reduced at last she said, she hastily picked him on the autumn, when he fainted again), she rubbed its face this morning. Now you unwound every bit of your faults.
        #  Number two: you play chess? Now, don't make such beautiful things that what they hold you! What's that rate. I'd far rather go without them than she was a voice as brightly as possible. For instance, the words go the Queen were thirsty, were you?
        #  How nice it up the white kitten had got back of my child!"
# print(markov(FILENAME))
