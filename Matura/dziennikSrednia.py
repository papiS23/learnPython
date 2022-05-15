file = open('doDziennikSrednia.txt', 'r')

fileCopy = []
for line in file:
    fileCopy.append(line.strip())

averages = []
for i in range(1, len(fileCopy)):
    grates = fileCopy[i].split()[1:]
    sumaOcen = 0
    for grate in grates:
        sumaOcen += int(grate)
    averages.append(round(sumaOcen/len(grates), 2))
averages.sort()

print(averages[-1])
