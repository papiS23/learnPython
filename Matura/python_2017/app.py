plik = open('przyklad.txt', 'r')
plikKopia = []
for linia in plik:
    plikKopia.append(linia.strip())

najjasniejszy = 0
najciemniejszy = 255

for linia in plikKopia:
    linia = linia.split()
    for pixel in linia:
        if int(pixel) > najjasniejszy:
            najjasniejszy = int(pixel)
        if int(pixel) < najciemniejszy:
            najciemniejszy = int(pixel)

print('6.1: ', najciemniejszy, najjasniejszy)

ileUsunac = 0
for linia in plikKopia:
    pierwszePol = linia.split()[0:160]
    drugiePol = linia.split()[160:320]
    if not pierwszePol == drugiePol[::-1]:
        ileUsunac += 1
print('6.2: ', ileUsunac)

calyObraz = []
for linia in plikKopia:
    calyObraz.append(linia.split())

ileKontrastujacych = 0
for indexKolumn in range(1, 198):
    for i in range(1, 318):
        if abs(int(calyObraz[indexKolumn][i]) - int(calyObraz[indexKolumn][i + 1])) >= 128:
            ileKontrastujacych += 1
        if abs(int(calyObraz[indexKolumn][i]) - int(calyObraz[indexKolumn + 1][i])) >= 128:
            ileKontrastujacych += 1
for i in range(0, 200)
    if abs(int(calyObraz[i][0]) - int(calyObraz[i+1][0])) >= 128:
        ileKontrastujacych += 1