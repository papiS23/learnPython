def valid_parentheses(string):
    parenthases = ''
    for char in string:
        if char == '(' or char == ")":
            parenthases += char
    for i in range(len(parenthases)):
        if parenthases[i] == '(' and parenthases[-(i+1)] == ')':
            continue
        elif parenthases[i] == ')' and parenthases[-(i+1)] == '(':



## (()(()))