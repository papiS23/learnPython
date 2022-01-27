def order(sentence):
    words = sentence.split()
    result = []
    for i in range(1, len(words)+1):
        for word in words:
            if str(i) in word:
                result.append(word)
    return ' '.join(result)

print(order('mar3k s1ema t2u'))