import math

slowo = input("Podaj slowo: ")

def czyPalindrom(word):
    wordList = []
    for i in range(len(word)):
        wordList.append(word[-(i+1)])
    word2 = ''.join(wordList)
    if word == word2:
        return True
    else:
        return False

if czyPalindrom(slowo):
    print(f'{slowo} jest palindromem')
else:
    print(f'{slowo} nie jest palindromem')
