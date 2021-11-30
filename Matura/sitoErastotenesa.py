liczba = int(input("Podaj liczbe: "))

liczby = []
for i in range(2, liczba+1):
    liczby.append(i)

print(liczby)

for n in liczby:
    z = 0
    if n != 0:
        for j in range(0,len(liczby),n):
            if j != 0:
                liczby[j] = 0

suma = 0
print(liczby)
for num in liczby:
    suma = suma + num
print(suma)