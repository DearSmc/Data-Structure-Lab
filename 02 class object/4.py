arr = list(map(int,input("Enter Your List : ").split()))
res =[]

if(len(arr)<3):
    print("Array Input Length Must More Than 2")
else:
    if(sum(arr)==0) :
        res.append([0,0,0])
    else:
        for i in range (len(arr)):
            for j in range (i+1,len(arr)):
                for k in range (j+1,len(arr)):
                    if(arr[i]+arr[j]+arr[k] == 0):
                        res.append([arr[i],arr[j],arr[k]])
print(res)