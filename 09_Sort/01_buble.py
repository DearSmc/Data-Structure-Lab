def bubble(a, i, count):
    global n
    # print(a)
    if n-1 == count:
        # print("*")
        return

    if i == len(a)-1:
        # print("3")
        bubble(a, 0, count+1)
    elif a[i] > a[i+1]:
        # print("2")
        a[i], a[i+1] = a[i+1], a[i]
        bubble(a, i+1, count)
    else:
        # print("1")
        bubble(a, i+1, count)


inp = list(map(int, input("Enter Input : ").split()))
# print(inp)
n = len(inp)
bubble(inp, 0, 0)
print(inp)
