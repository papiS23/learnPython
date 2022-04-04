ip = input("Podaj IP: ").split('.')
maska = input("Podaj maska: ").split('.')

print('')
print('------------------------')
print('')

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
        wynik.append(str(int(ip[i]) & int(maska[i])))
    return wynik

def adresBroadcast(ip, maska):
    broadcast = []
    for i in range(4):
        broadcast.append(str(int(ip[i]) + (255-int(maska[i]))))
    return broadcast

def iloscHostow(maska):
    maskaBin = ''
    for el in maska:
        maskaBin += bin(int(el))[2:]
    return 2**(32-maskaBin.count('1'))

def klasaIp(ip):
    if int(ip[0]) >= 1 and int(ip[0]) <= 126:
        return 'A'
    elif int(ip[0]) >= 128 and int(ip[0]) <= 191:
        return 'B'
    elif int(ip[0]) >= 192 and int(ip[0]) <= 223:
        return 'C'
    elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
        return 'D'
    elif int(ip[0]) >= 240 and int(ip[0]) <= 255:
        return 'E'

if czyOk(ip, maska):
    print('Adres IP: ', '.'.join(ip))
    print('Maska podsieci: ', '.'.join(maska))
    print('Adres sieci: ', '.'.join(adresSieci(ip, maska)))
    print('Adres broadcast: ', '.'.join(adresBroadcast(adresSieci(ip, maska), maska)))
    print('Ilosc hostow: ', iloscHostow(maska))
    print('Klasa IP: ', klasaIp(ip))