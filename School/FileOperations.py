file = open('file.txt', 'r') # Plik otwarty w trybie odczytu (r)
line1 = file.readline() # Odczytanie pierwszej lini
line_rest1 = file.readlines() # odczytanie reszty linijek i dodanie do listy
line_rest = []

for line in line_rest1:
    line_rest.append(line.strip()) # pozbycie sie znaku przejscia do nastepnej lini (\n) i dodanie do nowej listy

line1_str_numbers = line1.split() # Podzielenie pierwszej lini na liste z numerami ale w postaci tekstowej

line1_numbers = []
for numbers in line1_str_numbers:
    line1_numbers.append(int(numbers)) # zamiana liczb w postaci tekstowej na liczbowa i dodanie do nowej listy

def czyPierwsza(liczba):
    if liczba == 1:         # 1 nie jest liczba pierwsza wiec na poczatku trzeba sprzwdzic
        return False
    else:
        for i in range(2, liczba):
            if liczba % i == 0: # Sprawdzenie czy podana liczba dzieli sie przez liczby z zakresu od 2 do wartosci danej liczby
                return False    # jezeli tak to oznacza ze nie jest pierwsza, zwraca false i konczy dalsze wykonywanie funkcji
        return True             # jezeli przez nic sie nie dzieli zwraca true czyli jest pierwsza

def dlugoscSlowa(slowo):
    return len(slowo)

def czyPalindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    else:
        return False

# Zadanie z liczbami pierwszymi
print('Liczby pierwsze:', end=" ")
for num in line1_numbers:       # jak by w zadaniu bylo wypisac ilosc liczb pierwszych to zamiast tego na dole dodajemy je do listy i sprawdzamy jej dlugosc za pomoca len(lista)
    if czyPierwsza(num):
        print(num, end=", ")
print() # przejscie do nastepnej lini

# Zadanie ze sprawdzeniem dlugosci slowa
print(f"Dlugosc slowa {line_rest[0]} wynosi: {dlugoscSlowa(line_rest[0])}") #uzycie f przed "" pozwala na uzywanie kodu pythona w {} pomiedzy slowami

# Zadanie z palindromami
for word in line_rest:
    if czyPalindrom(word):
        print(f"{word} jest palindromem")
    else:
        print(f"{word} nie jest palindromem")