inp = input("Enter Input : ").split(",")
# print(inp)

lst=[]
for i in inp:
    if i!='D':
        if "EN" in i:
            lst.append(i)
        elif "ES" in i:
            if len(lst)==0:
                lst.append(i)
            else:
                j=0
                while("ES" in lst[j]):
                    j+=1
                    if j==len(lst):
                        break
                lst.insert(j,i)
    else:
        if len(lst) > 0:
            print(lst.pop(0)[3:])
        else:
            print("Empty")
