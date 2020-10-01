# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# 'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
# 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'

ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
         'R','S','T','U','V','W','X','Y','Z']

ORDERED = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
           'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

TEST_CIPHER = "ID EWKKF WDQSMDU ID JCW JIEW XB XSU, OCWD QXXU PIDQ CWDKF JCW NWAXDU KGSWU JCW SMDU, JCWKW SIHWU OIJCID JCW QKWWD QSMUWN XB NCWKOXXU BXKWNJ, DWMK DXJJIDQCME JXOD, M BMEXGN XGJSMO OCXNW DMEW OMN KXYID CXXU. DX MKACWK WHWK SIHWU JCMJ AXGSU NZWWU M QKMF QXXNW NCMBJ OIJC NGAC NPISS MDU AGDDIDQ MN CIN, DXK OWKW JCWKW WHWK NGAC FWXEWD MN JCW NWHWDNAXKW EWKKF EWD JCMJ KXMEWU OIJC CIE JCKXGQC JCW QKWWDOXXU NCMUWN. KIQCJ EWKKISF JCWF UOWSSWU OIJCID JCW UWZJCN XB NCWKOXXU BXKWNJ, NGBBWKIDQ DWIJCWK AMKW DXK OMDJ, YGJ ZMNNIDQ JCW JIEW ID EWKKF QMEWN XB MKACWKF XK YXGJN XB AGUQWS ZSMF, SIHIDQ GZXD JCW PIDQ'N HWDINXD, OMNCWU UXOD OIJC UKMGQCJN XB MSW XB XAJXYWK YKWOIDQ."

FILE_NAME = 'ciphertext.txt'

def cipher(text,code):
    """
    Takes a text to encode/decode and a dict of letters to swap e.g. {'A':'H'}
    Returns the encoded or decoded text
    """
    encoded = ''
    for letter in text:
        if letter in code:
            encoded += code[letter]
        else:
            encoded += letter
    return encoded


def find_freq(text):
    """
    Returns a dict of the frequency of letters e.g. {'A':485}
    """
    freq = {}
    for letter in ALPHA:
        freq[letter] = 0
    for letter in text:
        if letter in ALPHA:
            freq[letter] += 1
    return freq


def order_by_freq(data):
    """
    Takes a dict of key=letter, val=Frequency
    Returns a list of keys ordered by Frequency
    """
    return sorted(data, key=data.get, reverse=True)


def match_letters(data):
    new_dict = {}
    for i in range(len(ORDERED)):
        new_dict[data[i]] = ORDERED[i]
    return new_dict

f = open(FILE_NAME, "r")
ciphertext = f.read()
freq = find_freq(ciphertext)
print(freq)
ordered_chars = order_by_freq(freq)
print(ordered_chars)
ciphert = match_letters(ordered_chars)
print(cipher(ciphertext,ciphert))
