def dirReduc(arr):
    arrCopy = arr.copy()
    def reduction(directions):
        for i in range(len(directions)):
            if i < len(directions) - 1:
                if directions[i] == 'NORTH' and directions[i + 1] == 'SOUTH':
                    directions[i] = ''
                    directions[i + 1] = ''
                elif directions[i] == 'SOUTH' and directions[i + 1] == 'NORTH':
                    directions[i] = ''
                    directions[i + 1] = ''
                elif directions[i] == 'EAST' and directions[i + 1] == 'WEST':
                    directions[i] = ''
                    directions[i + 1] = ''
                elif directions[i] == 'WEST' and directions[i + 1] == 'EAST':
                    directions[i] = ''
                    directions[i + 1] = ''
    reduction(arrCopy)
    while arrCopy.count('') > 0:
        for way in arrCopy:
            if way == '':
                arrCopy.remove(way)
        reduction(arrCopy)
    return arrCopy

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))