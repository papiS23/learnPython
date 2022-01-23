def DNA_strand(dna):
    result = ''
    for letter in dna:
        if letter == "A":
            result = result + "T"
        elif letter == "T":
            result = result + "A"
        elif letter == "G":
            result = result + "C"
        elif letter == "C":
            result = result + "G"
    return result