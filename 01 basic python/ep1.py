print("*** Converting hh.mm.ss to seconds ***")
print("Enter hh mm ss : ",end="")
h,m,s = input().split()
h = int(h)
m = int(m)
s = int(s)

if(m>=60 or m<0):
    print("mm(" + str(m) + ") is invalid!")
elif(s>=60 or s<0):
    print("ss(%d) is invalid!" %s)
else:
    sum= str((((h*60)+m)*60)+s)

    if(h<10):
        h='0'+str(h)
    else:
        h=str(h)

    if(m<10 and m>=0):
        m='0'+str(m)
    else:
        m=str(m)
        
    if(s<10):
        s='0'+str(s)
    else:
        s=str(s)

    print(h,m,s, sep=':', end=" = ")
    '''
    n=len(sum)
    i=0
    for x in sum: 
        print(x,end="")
        if(i==((n%3)-1) and n>3):
            print(",",end="")
        i+=1
    '''
    newSum = '{:,}'.format(int(sum))
    print(newSum + " seconds")
    
