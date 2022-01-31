def rgb(r, g, b):
    rgbArr = [r, g, b]
    hexa = []
    for col in rgbArr:
        if col < 0:
            hexa.append('00')
        elif col > 255:
            hexa.append('FF')
        elif len(hex(col)[2:]) < 2:
            hexa.append('0'+hex(col)[2:].upper())
        else:
            hexa.append(hex(col)[2:].upper())
    return ''.join(hexa)

print(rgb(255, 0, 255))