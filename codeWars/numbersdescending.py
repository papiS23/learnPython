def descending_order(num):
    str_number = str(num)
    num_list = []
    for n in str_number:
        num_list.append(n)
    num_list.sort(reverse=True)
    return int(''.join(num_list))

print(descending_order(123456789))