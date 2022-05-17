def szyfrowanie(slowo, klucz):
    klucz = int(klucz) % 26
    wynik = ''
    for litera in slowo:
        if ord(litera)+klucz > 122:
            wynik += chr(ord(litera)+klucz-26)
        else:
            wynik += chr(ord(litera)+klucz)
    return wynik

def deszyfrowanie(slowo, klucz):
    klucz = int(klucz) % 26
    wynik = ''
    for litera in slowo:
        if ord(litera)-klucz >= 97:
            wynik += chr(ord(litera)-klucz)
        else:
            wynik += chr(ord(litera)-klucz+26)
    return wynik

print(deszyfrowanie('eolqudyaiguw', 124))
print(ord('z'))