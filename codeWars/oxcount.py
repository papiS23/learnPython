def xo(s):
    xcount = 0
    ocount = 0
    for i in str(s):
        if i == "x" or i == 'X':
            xcount += 1
        elif i == 'o' or i == 'O':
            ocount += 1
    if xcount == ocount:
        return True
    else:
        return False