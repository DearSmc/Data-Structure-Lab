def bi_seach(lst,x,l,r):
    m = (l+r)//2
    if lst[m] == x:
        return m
    elif lst[m] > x:
        return bi_seach(lst,x,l,m-1)
    else:
        return bi_seach(lst,x,m+1,r)
    
lst = list()


for i in range (0,57,3):
    lst.append(i)
print(lst)
print(bi_seach(lst,27,0,len(lst)-1))
        

