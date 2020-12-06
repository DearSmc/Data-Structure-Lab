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

neg = list()
neg_i = list()

for i in range(len(inp)):
    if inp[i] < 0:
        neg.append(inp[i])
        neg_i.append(i)
for j in neg_i[::-1]:
    inp.pop(j)

# print(inp)
# print(neg,neg_i)
if len(inp) != 0:
    n = len(inp)
    bubble(inp, 0, 0)
    # print(inp)

for i in neg_i:
    inp.insert(i, neg[0])
    neg.pop(0)
# print(inp)
for i in inp:
    print(i, end=" ")
