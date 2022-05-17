def test(a, b, c):
    print(type(a), type(b), type(c))

test('8','7','6')

def siema(imie="marek"):
    print("siema", imie)

siema('bartek')

tekst = 'siema tu bartek ale to ala ma kota'

t = [x for x in tekst if not x == ' ']

print(t)