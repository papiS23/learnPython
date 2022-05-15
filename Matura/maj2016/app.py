plik = open('dane_6_2.txt', 'r')

for linia in plik:
    poSzyfrowaniu = ''
    for litera in linia:
        numerZnaku = 65
        if ord(litera) + 107%26 > 90:
            numerZnaku += ord(litera) + 107%26 - 90
        else:
            numerZnaku = ord(litera) + 107%26
        poSzyfrowaniu += chr(numerZnaku)
    print(poSzyfrowaniu)
