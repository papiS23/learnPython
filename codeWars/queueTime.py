def queue_time(customers, n):
    tills = []
    for i in range(n):
        tills.append(0)
    for customer in customers:
        tills.sort()
        tills[0] += customer
    tills.sort()
    return tills[-1]


print(queue_time([2,2,3,3,4,4],2))

