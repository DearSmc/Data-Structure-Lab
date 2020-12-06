import math


def get_next_index(lst, value, n, max_try):
    a = [0]*(n+1)
    try_ = 0
    a[0] = value
    # for x in lst:
    #    print(x)
    print("collision number {} at {}".format(try_+1, a[0]))
    while try_ < max_try-1:
       
        try_ += 1
        a[try_] = (a[try_-1] + try_*2-1) % n
        # print("debug", a)
        # print("{} = ({} + {}) % {}".format(arr[try_],arr[try_-1],try_*try_ ,n))
        if lst[a[try_]] == None:
            return a[try_]
        else:
            print("collision number {} at {}".format(try_+1, a[try_]))

    # print(arr)
    return -1

# F(i) = F(i-1) + 2*i - 1




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
    global prevData
    global arr
    print("rehash()")
    tableSize = nextPrime(tableSize)
    arr = [None]*tableSize
    for j in range(len(prevData)):
        print("j")
        if arr[j%tableSize] == None: 
            arr[j%tableSize] = prevData[j]
        else:
            addData(prevData[j])
    prevData = arr.copy()

def addData(data):
    global tableSize
    global prevData
    global arr
    global currentSize
    global maxColis
    print("add DAta")
    if arr[data%tableSize] == None:
        arr[data%tableSize] = data
        prevData[data%tableSize] = data
        currentSize += 1
    else:
        index = get_next_index(arr, data % tableSize, tableSize, maxColis)
        while(index == -1):
            print("****** Max collision - Rehash !!! ******")
            # print("2", arr, i, tableSize, maxColis)
            reHash()
            if arr[data % tableSize] == None:
                arr[data % tableSize] = data
                prevData[data % tableSize] = data
                currentSize += 1
                break
            else:
                index = get_next_index(arr, data % tableSize, tableSize, maxColis)
            # print("2", arr, i, tableSize, maxColis)

        if index != -1:
            arr[index] = data
            prevData[index] = data
            currentSize += 1


def showTable(k):
    global data
    if k == -1:
        print("Initial Table :")
    for k in range(0, len(arr)):
        print("#"+str(k+1), end="\t")
        print(arr[k])
    print("---------------------------")

c, d = input(" ***** Rehashing *****\nEnter Input : ").split('/')
tableSize, maxColis, threshold = map(int, c.split())
data = list(map(int, d.split()))

currentSize = 0
arr = [None]*tableSize
prevData = [None]*tableSize



showTable(-1)
for i in data:
    # print("Add :", i, "currenSize =", tableSize, " -> ", i % tableSize)
    print("Add :", i)
    if ((currentSize+1) / tableSize) * 100 >= threshold:
        print("****** Data over threshold - Rehash !!! ******")
        reHash()
        addData(i)
             
    else:
        if currentSize != tableSize:
            addData(i)
        else:
            print("This table is full !!!!!!")
            break

    showTable(i)
