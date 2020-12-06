inp = input("Enter : ").split(",")
node = set()
adj = dict()
for i in inp:
    a,b = i.split()
    if a not in adj.keys():
        adj[a] = [b]
    else:
        adj[a].append(b)
    
    if b not in adj.keys():
        adj[b] = [a]
    else:
        adj[b].append(a)

for i in adj.keys():
    adj[i] = sorted(adj[i])

# print(adj)



cheak = dict()

def dfs(v):
    if v not in cheak.keys():
        cheak[v] = True
        print(v,end=" ")
        for i in adj[v]:
            dfs(i)
        
print("Depth First Traversals : ",end="")
dfs(min(adj.keys()))

for i in sorted(adj.keys()):
    dfs(i)


print("\nBredth First Traversals : ",end="")
cheakB = dict()
for i in sorted(adj.keys()):
    q = [i]
    while q:
        temp = q.pop(0)
        if temp not in cheakB.keys():
            cheakB[temp] =True
            print(temp,end=" ")
            for j in adj[temp]:
                q.append(j)


