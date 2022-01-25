def find_short(s):
    words = s.split()
    l = len(words[0])
    for word in words:
        if len(word) < l:
            l = len(word)
    return l

print(find_short('siema siema pozdrowienia za podziemia'))