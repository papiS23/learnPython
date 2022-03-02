def isPinCorrect(pin):
    return len(str(pin)) in (4, 6) and str(pin).isdigit()

print(isPinCorrect('33a3'))