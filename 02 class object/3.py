typ,text,mode = input("*** Odd Even ***\nEnter Input : ").split(",")

if(typ == "L"):
    text = list((text.split()))
    res = []
#print(text)

def odd_even(arr, o):
    if o:
        for i in range(0,len(arr),2):
            if type(arr) == list:
                res.append(arr[i])
            else:
                print(arr[i],end="")
             
    else:
        for i in range(1,len(arr),2):
            if type(arr) == list:
                res.append(arr[i])
            else:
                print(arr[i],end="")

    if type(arr) == list:
        print(res)  
           
if(mode == "Odd"):
    odd_even(text,True)
elif(mode == "Even"):
    odd_even(text,False)

    