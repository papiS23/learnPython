# num_1 = int(input("Podaj pierwsza liczbe: "))
# action = input("Podaj dzialanie (*, /, ^, +, -): ")
# num_2 = int(input("Podaj druga liczbe: "))
#
#
# if(action == "+"):
#     print(f"Wynik dodawania to: {num_1+num_2}")
# elif(action == "-"):
#     print(f"Wynik odejmowania to: {num_1-num_2}")
# elif (action == "*"):
#     print(f"Wynik mnożenia to: {num_1*num_2}")
# elif (action == "/"):
#     print(f"Wynik dzielenia to: {num_1/num_2}")
# elif (action == "^"):
#     print(f"Wynik potęgowania: {pow(num_1, num_2)}")
# else:
#     print("Niepoprawne działanie")
some_numbers = [1, 3, 5, 7, 9, 0]
friends = ['marysia', 'dominik', 'pawel', 'blazej', 'wojtek', 'michal']
friends.extend(some_numbers)
# print(friends)
reverse_table = []
for num in some_numbers:
    reverse_table.insert(0, num)

print(reverse_table)
# for i in range(6):
#     some_numbers[i] = some_numbers[i] + 1
# print(some_numbers)



# for item in table:
#     print(item)
# for i in range(5):
#     table.append(i)
#     print(table)
from math import *
# print(floor(3.89))
