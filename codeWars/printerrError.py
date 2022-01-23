def printer_error(s):
    alphabet = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    error_count = 0
    for letter in s:
        for n in alphabet:
            if n == letter:
                error_count += 1
                continue
    return f"{error_count}/{len(s)}"