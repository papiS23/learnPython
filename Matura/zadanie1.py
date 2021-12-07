liczby = []
for i in range(101):
    if i % 3 == 0 and i != 0:
        liczby.append("@")
    elif i % 5 == 0 and i != 0:
        liczby.append("#")
    elif i % 5 == 0 and i % 3 == 0 and i != 0:
        liczby.append("`-`")
    else:
        liczby.append(i)

print(liczby)