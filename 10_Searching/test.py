import math


def nextPrime(n):
    i = 2*n
    while True:

        cheak = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                cheak += 1

        if cheak:
            i += 1
        else:
            break

    return i


def reHash():
    global tableSize
    global pre
    global arr
    tableSize = nextPrime(tableSize)
    arr = [None]*tableSize
    for j in range(len(pre)):
        arr[j] = pre[j]

    pre = arr.copy()


tableSize = 3
arr = [1, 2, 3]
pre = [1, 2, 3]

reHash()
print(arr)
print(pre)
