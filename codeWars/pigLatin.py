def pig_it(text):
    words_list = []
    for word in text.split():
        if word == '!' or word == '.' or word == '?':
            words_list.append(word)
        else:
            words_list.append(word[1:] + word[0] + 'ay')
    return ' '.join(words_list)

print(pig_it('siema siema pozdrowienia z podziemia'))
