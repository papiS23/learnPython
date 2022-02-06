def valid_parentheses(string):
    parenthases = []
    for char in string:
        if char == '(' or char == ")":
            parenthases.append(char)
    counter = 0
    while counter == 0:
        length = len(parenthases)
        print(parenthases)
        for i in range(len(parenthases)-1):
            if parenthases[i] == '(' and parenthases[i+1] == ')':
                parenthases.remove(parenthases[i])
                parenthases.remove(parenthases[i])
                break
        if len(parenthases) == length:
            counter = 1
    if len(parenthases) == 0:
        return True
    else:
        return False

## funkcja zwraca true a nie powinna, usuwane sa elementy ktore nie powinny
print(valid_parentheses("())(()"))