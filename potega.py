def potega(num1, wykladnik):
    wynik = 1
    for i in range(wykladnik):
        wynik = wynik * num1
    return wynik

print(potega(7, 5))