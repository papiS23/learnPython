import random
import time

def euklides(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

print("Algorytm Euklidesa: ", euklides(99, 21))

def fibonacci(n):
    n = int(n)
    if n <= 0:
        return "Ciag musi miec dlugosc wieksza od 0"
    c = 1
    b = 0
    s = 0
    fibList = []
    for i in range(n):
        s = b + c
        c = b
        b = s
        fibList.append(s)
    return fibList;

print("Ciag fibonacciego:",fibonacci(10))


def randomIntList(listRange):
    listRange = int(listRange)
    randList = []

    for i in range(listRange + 1):
        randList.append(random.randint(1, listRange))
    return randList

def findMinMax(list):
    start = round(time.time(), 5)
    min = list[0]
    max = list[0]

    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        elif list[i] < min:
            min = list[i]

    end = round(time.time(), 5)
    complexity = end - start
    return min, max, list, complexity

print("Najwieksza i najmniejsza liczba z listy:", findMinMax(randomIntList(10)))

def bubbleSort(list):
    start = round(time.time(), 5)
    stillSort = 1
    while stillSort == 1:
        stillSort = 0
        for i in range(len(list) - 1):
            if list[i + 1] < list[i]:
                temp = list[i + 1]
                list[i+1] = list[i]
                list[i] = temp

                stillSort = 1

    end = round(time.time(), 5)
    complexity = end - start

    return list, complexity

print("Sortowanie babelkowe:",bubbleSort(randomIntList(30)))


def insertSort(list):
    start = round(time.time(), 5)
    i = 1
    while i < len(list):
        j = i
        while j > 0 and list[j-1] > list[j]:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j -= 1
        i += 1

    end = round(time.time(), 5)
    complexity = end - start

    return list, complexity

print("Sortowanie przez wstawianie:",insertSort(randomIntList(30)))

