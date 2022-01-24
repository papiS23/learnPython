def accum(s):
    result = s[0].upper()
    for i in range(len(s)-1):
        result = result + f'-{s[i+1].upper()}{s[i+1].lower()*(i+1)}'
    return result

print(accum('bartekimarysia'))