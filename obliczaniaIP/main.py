ip = input("Podaj IP: ").split('.')
maska = input("Podaj maska: ").split('.')

def czyOk(ip, maska):
    for el in ip:
        if not (int(el) <= 255 or int(el) >= 0):
            print("Wprowadzono bledne IP.")
            return False

    maskaBin = ''
    for el in maska:
        maskaBin += bin(int(el))[2:]
        if not (int(el) <= 255 or int(el) >= 0):
            print('Wprowadzono bledna maske.')
            return False
    for i in range(len(maskaBin)):
        if maskaBin[i] == '0':
            if '1' in maskaBin[i:]:
                print('Wprowadzono bledna maske')
                return False
    return True

def adresSieci(ip, maska):
    wynik = []
    for i in range(4):
        ipBin = int(bin(int(ip[i]))[2:])
        maskaBin = int(bin(int(maska[i]))[2:])
        wynik.append(ipBin & maskaBin)
    return wynik

if czyOk(ip, maska):
    print('Adres IP: ', '.'.join(ip))
    print('Maska podsieci: ', '.'.join(maska))
    print(adresSieci(ip, maska))