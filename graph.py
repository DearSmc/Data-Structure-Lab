def dfs(g,fro,check):
    if check[fro]:
        return
    cheak[fro] = True
    print(fro,end=" ")
    for i in g.get(fro,[]):
        dfs(g,i,check)

def bfs(g,fro,check):
    q = [fro]
    while q:
        temp = q.pop(0)
        if check[temp]:
            continue
        check[temp] = True
        print(temp,end=" ")
        for i in g.get(temp,[]):
            q.append(i)

inp = input("Enter : ").split(",")
g = dict()
# vertex = set()
check = dict()
for i in inp:
    a = i.split()
    if a[0] not in g.keys():
        g[a[0]] = []

    g[a[0]].append(a[1])
    check[a[0]] = False
    check[a[1]] = False
    # vertex.add(a[0])
    # vertex.add(a[1])

# n = len(vertex)
# print(check)
for i in g.keys():
    g[i].sort()

print(g)
# print("DFS :",end=" ")
# dfs(g,list(g)[0],check)
print("BFS :",end=" ")
bfs(g,list(g)[0],check)