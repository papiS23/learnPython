def order_weight(strng):
    numbersList = []
    for num in strng.split():
        sum = 0
        for digit in num:
            sum += int(digit)
        numbersList.append(sum)
    oldNumberList = numbersList
    numbersList.sort()
    newList = []
    for n in numbersList:
        newList.append(oldNumberList[oldNumberList.index(str(n))])
    return newList




print(order_weight("103 123 4444 99 2000"))