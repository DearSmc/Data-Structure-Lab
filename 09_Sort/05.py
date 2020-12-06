def selectionSort(inp):
    for i in range(len(inp)):
        minIndex = i
        for j in range(i, len(inp)-1):
            if inp[minIndex] >= inp[j+1]:
                minIndex = j+1
        inp[minIndex], inp[i] = inp[i], inp[minIndex]
    return inp


def twoBit(x):
    if x == len(inp):
        sum = 0
        for i in range(len(inp)):
            sum += inp[i]*a[i]
        # print(a)
        # print(a, sum,n,sum == n)
        if sum == n:
            lst = list()
            for i in range(len(inp)):
                if a[i] == 1:
                    lst.append(inp[i])
            subset.append(lst)

    else:
        a[x] = 0
        twoBit(x+1)
        a[x] = 1
        twoBit(x+1)


def sortBySize(inArr):
    arr = list()
    for i in range(1, len(inp)+1):
        for j in inArr:
            if len(j) == i:
                if len(arr) > 0:
                    cur = len(arr)-1
                    if len(arr[cur]) != i:
                        arr.append(j)
                    else:
                        notSet = True
                        while cur >= 0 and len(arr[cur]) == i and notSet:
                            for k in range(0, len(j)):
                                if j[k] > arr[cur][k]:
                                    arr.insert(cur+1, j)
                                    notSet = False
                                elif j[k] < arr[cur][k]:
                                    cur -= 1
                                    break
                        if notSet:
                            arr.insert(cur+1, j)
                else:
                    arr.append(j)

    return arr

n, inp = input("Enter Input : ").split('/')
inp = selectionSort(list(map(int, inp.split())))
#inp = list(reversed(inp))
n = int(n)
a = [0]*len(inp)
# print(inp)
subset = list()
twoBit(0)
# print(subset)
subset = sortBySize(subset)
if len(subset) > 0:
    for i in subset:
        print(i)
else:
    print("No Subset")
