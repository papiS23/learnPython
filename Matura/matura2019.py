plik = open('przyklad.txt', 'r')
plikCopia = []
for linia in plik:
    plikCopia.append(linia.strip())

licznikLini = 0
wynik1 = ''
for linia in plikCopia:
    licznikLini += 1
    if licznikLini % 40 == 0:
        wynik1 += linia[9]
print(wynik1)



slowa = []
dlugosc = 0
for linia in plikCopia:
    licznik = 0
    for i in range(len(linia)):
        if linia[i] not in linia[:i]:
            licznik += 1
    if licznik > dlugosc:
        dlugosc = licznik
        slowa.clear()
        slowa.append(linia)
    elif licznik == dlugosc:
        slowa.append(linia)

print(slowa, dlugosc)