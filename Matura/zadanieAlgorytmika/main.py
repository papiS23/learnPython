plik = open('dane.txt', 'r')
kopiaPlik = []
for linia in plik.readline().split():
    kopiaPlik.append(int(linia))

najnizsza = 9999999999
najwieksza = 0
najwiekszyMnoznik = 0
for num in kopiaPlik:
    if num < najnizsza:
        for i in range(kopiaPlik.index(num)+1, len(kopiaPlik)):
            mnoznik = kopiaPlik[i]/najnizsza
            if mnoznik > najwiekszyMnoznik:
                najwiekszyMnoznik = mnoznik
                najwieksza = kopiaPlik[i]
                najnizsza = num

kosztKupna = najnizsza*100000
kosztSprzedarzy = najwieksza*100000
zysk = kosztSprzedarzy-kosztKupna
print('Najmniejsza: ', najnizsza)
print('Najwieksza: ', najwieksza)
print('Mnoznik: ', najwiekszyMnoznik)
print('Zarobek: ', zysk)