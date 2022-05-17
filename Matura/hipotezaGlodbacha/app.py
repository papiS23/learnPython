plik = open('dane.txt', 'r')
plik_wykonawczy = [int(x.strip().split()[0]) for x in plik if int(x.strip().split()[0]) % 2 == 0]

def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba%i == 0:
            return False
    if liczba == 1:
        return False
    return True

wynik = []
for liczba in plik_wykonawczy:
    pierwsze = []
    for i in range(1, liczba):
        if czy_pierwsza(i):
            pierwsze.append(i)
    pary = []
    for pierwsza in pierwsze:
        for pierwsza1 in pierwsze:
            if pierwsza + pierwsza1 == liczba:
                pary.append([pierwsza, pierwsza1])
    najlepsza_para = 0
    najlepszy_index = 0
    for para in pary:
        if abs(para[0]-para[1])<najlepsza_para:
            najlepszy_index = para.index()
            najlepsza_para = abs(para[0]-para[1])
    # print(liczba, pary[najlepszy_index][0], pary[najlepszy_index][1], sep=';')
    wynik.append(str(liczba) + ';' + str(pary[najlepszy_index][0]) + ';' + str(pary[najlepszy_index][1]))
print(';'.join(wynik))


