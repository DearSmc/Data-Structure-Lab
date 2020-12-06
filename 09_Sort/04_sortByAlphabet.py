def selectionSort(inp, key):
    for i in range(len(key)):
        minIndex = i
        for j in range(i, len(key)-1):
            if key[minIndex] >= key[j+1]:
                minIndex = j+1
        inp[minIndex], inp[i] = inp[i], inp[minIndex]
        key[minIndex], key[i] = key[i], key[minIndex]
    return inp


inp = input("Enter Input : ").split()

key = list()

for i in inp:
    for j in i:
        if (j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z'):
            key.append(j)
            break

# print(key)
print(" ".join(selectionSort(inp, key)))
