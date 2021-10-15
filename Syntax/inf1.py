liczba1 = 120
liczba2 = 120

if liczba1>liczba2:
    print("if ->",end=" ")
    print(liczba1, "jest wieksza od", liczba2)
elif liczba2>liczba1:
    print("ELIF ->", end=" --- ")
    print(liczba2, "jest wieksza od", liczba1)
else:
    print("ELSE", end=" :) ")
    print(f"{liczba1} jest rowna {liczba2}")

for liczba in range(10):
    print(liczba)