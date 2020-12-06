def staircase(n,ch):
    global i
    if n>0:
        if i>=n:
            print(ch)
            return
        else:
            i += 1
            ch += "_"*(n-i) + "#"*i + '\n'

            staircase(n,ch)
    elif n==0:
        print("Not Draw!")
        return
    else:
        if i >= -n:
            print(ch)
            return
        else:
            
            ch += "_"*(i) + "#"*(-n-i) +  '\n'
            i += 1
            staircase(n,ch)
i = 0
ch = ""
staircase(int(input("Enter Input : ")),ch)
