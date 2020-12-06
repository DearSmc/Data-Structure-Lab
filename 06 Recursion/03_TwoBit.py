def twoBit(x):
    if x==inp:
        print("".join(map(str,a)))
    else:
        a[x] = 0
        twoBit(x+1)
        a[x] = 1
        twoBit(x+1)

inp = int(input("Enter Number : "))

if inp>=0:
    if inp==0:
        print("0")
    else:
        a = [0]*inp
        twoBit(0)
else:
    print("Only Positive & Zero Number ! ! !")