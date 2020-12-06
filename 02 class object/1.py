arr = input("Enter String : ")

res = []
ch = []

ch.append(arr[0])
res.append(0)

for i in range(1,len(arr)):
    cheak = False
    for j in range(len(ch)):
        if(arr[i] == ch[j]):
            res.append(j)
            cheak = True
    if(not cheak):
        ch.append(arr[i])
        res.append(ch.index(arr[i]))

print(res)
