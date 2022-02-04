def anagrams(word, words):
    result = []
    for word1 in words:
        if len(word1) == len(word):
            result.append(word1)
            for letter in word:
                if word.count(letter) != word1.count(letter):
                    result.pop(-1)
                    break
    return result



print(anagrams('abba', ['aacbb', 'abcd', 'bbada', 'dada']))