file = open('file_listy.txt', 'r')

literyPowt = []
for line in file:
    current_line = line.split()
    num = int(current_line[0])
    word = current_line[1]
    for letter in range(ord('a'), ord('z')+1):
        ilosc = word.count(chr(letter))
        if ilosc == num:
            literyPowt.append(chr(letter))
    if len(literyPowt) > 0:
        print(word, literyPowt)
        literyPowt = []