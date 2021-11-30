file = open("fileLiczbySzczesliwe.txt", 'r')

def zamien_na_tablice(number):
    liczba = str(number)
    tablica = []
    for cyfra in liczba:
        tablica.append(int(cyfra))
    return tablica

liczbySzczesliwe = []
ileSumSzczesliwe = []

sumy = []

for line in file:
    number_list = zamien_na_tablice(int(line))
    suma = 0
    ileSum = 0
    while suma != 1:
        suma = 0
        for num in number_list:
            suma = suma + (num*num)
        ileSum = ileSum + 1
        if suma == 1:
            liczbySzczesliwe.append(int(line))
            ileSumSzczesliwe.append(ileSum)
            sumy.clear()
        elif suma in sumy:
            suma = 1
        else:
            number_list = zamien_na_tablice(suma)
            sumy.append(suma)

print(f"Liczb szczesliwych w pliku: {len(liczbySzczesliwe)}")
print(f"Najwiecej sum ma liczba: {liczbySzczesliwe[ileSumSzczesliwe.index(max(ileSumSzczesliwe))]}")