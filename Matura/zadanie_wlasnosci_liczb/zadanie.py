plik = open('dane.txt', 'r')

def czySumaCyfrParzysta(liczba):
    suma = 0
    for cyfra in liczba.strip():
        suma += int(cyfra)
    if suma%2 == 0:
        return True
    return False
def czyWszystkieParzyste(liczba):
    for cyfra in liczba.strip():
        if not int(cyfra)%2 == 0:
            return False
    return True
def czyCiagNiemalejacy(liczba):
    poprzedniaCyfra = int(liczba.strip()[0])
    for cyfra in liczba.strip():
        if poprzedniaCyfra > int(cyfra):
            return False
        else:
            poprzedniaCyfra = int(cyfra)
    return True
def pierwszeTakieSame(liczba):
    for i in range(2, int(liczba.strip())):
        if int(liczba.strip())%i == 0:
            return False
    if liczba.strip()[0] == liczba.strip()[-1]:
        return True

zad1 = 0
zad2 = 0
zad3 = 0
zad4 = 0
for liczba in plik:
    if czySumaCyfrParzysta(liczba):
        zad1 += 1
    if czyWszystkieParzyste(liczba):
        zad2 += 1
    if czyCiagNiemalejacy(liczba):
        zad3 += 1
    if pierwszeTakieSame(liczba):
        zad4 += 1

print('1: ', zad1)
print('2: ', zad2)
print('3: ', zad3)
print('4: ', zad4)


