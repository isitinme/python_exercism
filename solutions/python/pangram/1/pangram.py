import string

def is_pangram(sentence):
    letters = list()
    for word in sentence.lower().split(' '):
        for c in word:
            if c in string.ascii_lowercase and c not in letters:
                letters.append(c)
    return len(letters) == len(string.ascii_lowercase)