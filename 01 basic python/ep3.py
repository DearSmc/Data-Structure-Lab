print("*** Election ***\nEnter a number of voter(s) : ",end="")
n = int(input())
# make list of zero
a =[]
i=0
for i in range(20):
    a.append(0)

x = list(map(int,input().strip().split(' ')))

for i in x:
    if(i>0 and i<=20):
        a[i-1] = a[i-1]+1

if(max(a) != 0):
    print(a.index(max(a))+1)
else:
    print("*** No Candidate Wins ***")
