n = int(input("Enter a positive number : "))
if n<=0:
    print(str(n)+" is too low.")
elif n>=16:
    print(str(n)+" is too high.")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1:
                print("%X "%(j),end="")
            elif j==1:
                print("%X "%(i),end="")
            elif j==n:
                print("%X "%(i-1),end="")
            elif i==n:
                print("%X "%(j-1),end="")
            else:
                print("  ",end="")
        print("")