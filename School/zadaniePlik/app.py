file = open('dane.txt', 'r')

samogloski = ['a', 'i', 'o', 'u', 'y', 'e']
zadanie1 = []
zadanie2 = []
zadanie3 = []
zadanie4 = []
zadanie5 = []

for line in file:
    current_line = line.split()
    num1 = int(current_line[0])
    num2 = int(current_line[1])

    zadanie2.append(num1)
    zadanie2.append(num2)

    for sign in range(2,len(current_line)):
        if current_line[sign].isalpha():
            zadanie1.append(current_line[sign])
            ileSamoglosek = 0
            if len(current_line[sign]) == num2:
                zadanie3.append(current_line[sign])
            for samogloska in samogloski:
                ileSamoglosek += current_line[sign].count(samogloska)
            if ileSamoglosek == 2:
                zadanie5.append(current_line[sign])
        else:
            zadanie2.append(int(current_line[sign]))

    for item in range(1, len(current_line)):
        if current_line[item].isdigit() and int(current_line[item]) < num1:
            zadanie4.append(current_line[item])

print(f"Zadanie 1: {', '.join(zadanie1)}")
print(f"Zadanie 2: {max(zadanie2)}, {min(zadanie2)}")
print(f"Zadanie 3: {', '.join(zadanie3)}")
print(f"Zadanie 4: {', '.join(zadanie4)}")
print(f"Zadanie 5: {', '.join(zadanie5)}")