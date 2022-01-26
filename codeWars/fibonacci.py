def fibonacci(signature, n):
    while len(signature) < n:
        newNum = signature[-1]+signature[-2]
        signature.append(newNum)
    return signature[:n]

fiArray = fibonacci([1, 1], 1000)

print('Golden ratio: ',fiArray[-1]/fiArray[-2])
