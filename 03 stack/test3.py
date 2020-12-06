inp = input(" *** Recite the multiplication table ***\nEnter pattern for child 1 to 3 (-1 for sep) : ").split("-1")
a = inp[0].strip().split()
b = inp[1].strip().split()
c = inp[2].strip().split()

print("Pattern for child 1 : "+" ".join(a)) 

print("Pattern for child 2 : "+" ".join(b))
print("Pattern for child 3 : "+" ".join(c))
count =1
i=j=k = 0
while 1:
    if a[i]==b[j] and a[i]==c[k]:
        print("They recite same multiplication table in "+str(count)+" days")
        break
    else:
        i+=1
        j+=1
        k+=1
        count+=1
        if i==len(a):   i=0
        if j==len(b):   j=0
        if k==len(c):   k=0
    if count>365:
        print("This year they never recite same multiplication table !!!")
        break