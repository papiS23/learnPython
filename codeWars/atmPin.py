def validate_pin(pin):
    if str(pin).isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False

print(validate_pin('665a'))