inp = input("Enter Input : ").split(",")
# print(inp)

lst = []
for i in inp:
    if i!='D':
        lst.append(i[2:])
        print(len(lst))
    else:
        if len(lst)!=0:
            print(lst.pop(0)+' 0')
        else:
            print("-1")
            
if len(lst)!=0:
    print(" ".join(lst))
else:
    print("Empty")      