def tribonacci(signature, n):
    while len(signature) < n:
        newNum = signature[-1]+signature[-2]+signature[-3]
        signature.append(newNum)
    return signature[:n]

print(tribonacci([1,1,1], 0))