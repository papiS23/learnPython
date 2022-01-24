def disemvowel(string_):
    word = string_
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for vowel in vowels:
        if vowel in word:
            word = word.replace(vowel, '')
    return word

print(disemvowel('bartek'))