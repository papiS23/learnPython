file = open("daneSlowa.txt", 'r')
samogloski = ['a','e', 'i', 'o', 'u', 'y']

for line in file:
    current_line = line.split()
    number = int(current_line[0])
    word = current_line[1]
    newWord = word
    deleteLetters = []
    for samogloska in samogloski:
        if number == word.count(samogloska):
            newWord = newWord.replace(samogloska, "")
            deleteLetters.append(samogloska)
    if len(deleteLetters) > 0:
        print(f"{newWord}, usunieto: {' ,'.join(deleteLetters)}")


