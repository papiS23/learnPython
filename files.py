file = open('file.txt', 'r')
f = file.readlines()
file_words = []
for line in f:
    if line[-1] == "\n":
        file_words.append(line[:-1])
    else:
        file_words.append(line)
print(file_words)