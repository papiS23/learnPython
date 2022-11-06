import math

def numConverter(num, base):
    if ',' in str(num):
        numTotal = str(num).split(',')[0]
        numFractal = float('0.' + str(num).split(',')[1])
    else:
        numTotal = int(num)
        numFractal = 0

    hexChars = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': "A",
        '11': "B",
        '12': "C",
        '13': "D",
        '14': "E",
        '15': "F",
    }
    numTotalResult = []
    numFractalResult = []

    while numTotal != 0:
        if int(base) == 16:
            numTotalResult.insert(0, hexChars[str(int(numTotal) % int(base))])
            numTotal = int(numTotal) // int(base)
        else:
            numTotalResult.insert(0, str(int(numTotal) % int(base)))
            numTotal = int(numTotal)//int(base)

    for i in range(9):
        if numFractal == 0:
            break

        if int(base) == 16:
            numFractalResult.append(hexChars[str(math.floor(numFractal * int(base)))])
            numFractal = (numFractal * int(base)) - math.floor(numFractal * int(base))
        else:
            numFractalResult.append(str(math.floor(numFractal * int(base))))
            numFractal = (numFractal * int(base)) - math.floor(numFractal * int(base))

    return ''.join(numTotalResult) + "," + ''.join(numFractalResult)
print(numConverter("128,128", 2))