plik = open('dane.txt', 'r')
f = plik.readlines()
plik.seek(0)
caly_plik = plik.read()
lines_list = []
for line in f:
    lines_list.append(line.strip())
print(lines_list)
print(caly_plik)