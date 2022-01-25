def duplicate_count(text):
    str = text.lower()
    count = 0
    for i in range(len(str)):
        if str.count(str[i]) > 1 and str[:i].count(str[i]) == 0:
            count += 1
    return count

print(duplicate_count('marysiassssssrssss'))