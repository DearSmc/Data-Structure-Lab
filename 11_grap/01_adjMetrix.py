inp = input("Enter : ").split(",")
node = set()

for i in inp:
    a,b = i.split()
    node.add(a)
    node.add(b)
node = sorted(list(node))

adj = []
for i in range (len(node)):
    temp = []
    for j in range (len(node)):
        temp.append('0')
    adj.append(temp)
# print(adj)
# print(node)
for i in inp:
    x,y = i.split()
    indexA,indexB = -1,-1
    for j in range(len(node)):
        if x == node[j]:
            indexA = j
    for k in range(len(node)):
        if y == node[k]:
            indexB = k
    adj[indexA][indexB] = '1'

# print(adj)            

print("    "+"  ".join(node))
for i in range(len(node)):
    print(node[i],":",", ".join(adj[i]))