# def cheakCycle(g):
#     n = len(g)
#     cheak = [False]*n
#     i = 0
#     q = []
#     q.append(i)
#     while q:
#         cheak[i] = True
#         for j in g[q]:
#             pass


# inp = input("Enter : ").split(",")
# a = []
# b = []
# for i in inp:
#     x,y = i.split()
#     a.append(int(x))
#     b.append(int(y))

# vertex = set()
# for i in range(len(a)):
#     vertex.add(a[i])
#     vertex.add(b[i])
# vertex = list(vertex)
# subG = [0]*len(vertex)
# g = []
# for i in range(len(vertex)):
#     g.append(subG.copy())

# for i in range(len(a)):
#     g[vertex.index(a[i])][vertex.index(b[i])] = 1
#     g[vertex.index(b[i])][vertex.index(a[i])] = 1
    
# print(g)

def checkpath(g, fr, p):
    if fr in p[:-1]:
        return True
    if fr not in g.keys():
        return False

    for i in g[fr]:
        t = checkpath(g, i, p + [i])
        
    return t

g = dict()
inp = input("Enter : ").split(',')
for i in inp:
    a = i.split()
    if a[0] not in g.keys():
        g[a[0]] = []
    g[a[0]].append(a[1])
if checkpath(g, list(g)[0], [list(g)[0]]):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")