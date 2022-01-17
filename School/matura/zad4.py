def sumaPotCyfry(liczba):
    wynik = 0
    while(liczba>0):
        cyfra = liczba%10
        wynik += cyfra*cyfra
        liczba = int(liczba/10)
    return wynik

def czyWesola(liczba):
    cykl = set()
    cykl.add(liczba)
    while(True):
        liczba = sumaPotCyfry(liczba)
        if (liczba == 1):
            return len(cykl)+1
        else:
            if liczba in cykl:
                return 0
            else:
                cykl.add(liczba)

# for liczba in range(1,1001):
#     if czyWesola(liczba):
#         print(czyWesola(liczba))

plik = open('liczby.txt', 'r')

ileWesolych = 0
for liczbaSTR in plik:
    liczba = int(liczbaSTR)
    if (czyWesola(liczba)>0):
        ileWesolych += 1

print(ileWesolych)