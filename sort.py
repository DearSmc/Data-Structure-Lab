def buble(lst):
    for i in range (len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1] , lst[j]
    return lst

def selection(lst):
    for i in range (len(lst)):
        mini  = 2000
        index = -1
        for j in range(i,len(lst)):
            if lst[j] < mini:
                index = j
                mini =  lst[j]
        lst[i] ,lst[index] = lst[index],lst[i]
    return lst

def insert(lst):
    for i in range(1,len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j-1]:
            lst[j] , lst[j-1] = lst[j-1] , lst[j]
            j -= 1
    return lst

def merge(lst,l,r):

    if l < r:
        m = ( l + r )// 2
        merge(lst,l,m)
        merge(lst,m+1,r)

        q1 ,q2 = lst[l:m+1],lst[m+1:r+1]

        while q1 and q2:
            if q1[0] < q2[0]:
                lst[l] = q1.pop(0)
            else:
                lst[l] = q2.pop(0)
            l+=1
            
        while q1:
            lst[l] = q1.pop(0)
            l+=1
        while q2:
            lst[l] = q2.pop(0)
            l+=1
    return lst

def quickSort(lst,l,r):
    if l < r:
        i,p = l,r
        for j in range(l,r):
            if lst[p] > lst[j]:
                lst[i] ,lst[j] = lst[j], lst[i]
                i += 1
            # j += 1

        lst[i] , lst[p] = lst[p] , lst[i]
        quickSort(lst,l,i-1)
        quickSort(lst,i+1,r)
    return lst



lst = [3,1,4,9,2,8,5,7,0,6]
# print(buble(lst))
# print(selection(lst))
# print(insert(lst))
# print(merge(lst,0,len(lst)-1))
print(quickSort(lst,0,len(lst)-1))

