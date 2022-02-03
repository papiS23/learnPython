plik = open('dane.txt', 'r')
numbers = []
for num in plik:
    numbers.append(int(num))

def ileNieparzystychJedynek(plik):
    nieparzysteBin = 0
    for num in plik:
        if bin(int(num))[2:].count('1') % 2 != 0:
            nieparzysteBin += 1
    return nieparzysteBin

def ileRosnacychOsemkowy(plik):
    rosnace = 0
    for num in plik:
        osem = oct(int(num))[2:]
        for i in range(len(osem)-1):
            if int(osem[i]) >= int(osem[i+1]):
                rosnace -= 1
                break
        rosnace += 1
    return rosnace

def najwiekszaIloscJedynekBin(plik):
    najwieksza = 0
    najwieksze = []
    for num in plik:
        if bin(int(num))[2:].count('1') > najwieksza:
            najwieksza = bin(int(num))[2:].count('1')
            najwieksze.clear()
            najwieksze.append(num)
        elif bin(int(num))[2:].count('1') == najwieksza:
            najwieksze.append(num)
    return najwieksza, najwieksze

def ciagLiczbHex(plik):
    ciag = []
    ciagTymczasowy = []
    licznik = 0
    for num in plik:
        if hex(num)[2:].isdecimal():
            if licznik == 0:
                ciagTymczasowy.append(num)
                licznik = 1
            else:
                ciagTymczasowy.append(num)
        else:
            licznik = 0
            if len(ciagTymczasowy) > len(ciag):
                ciag = ciagTymczasowy.copy()
            ciagTymczasowy.clear()
    return len(ciag), ciag

print("Zadanie 1: ",ileNieparzystychJedynek(numbers))
print("Zadanie 2: ",ileRosnacychOsemkowy(numbers))
print("Zadanie 3: ",najwiekszaIloscJedynekBin(numbers))
print("Zadanie 4: ",ciagLiczbHex(numbers))