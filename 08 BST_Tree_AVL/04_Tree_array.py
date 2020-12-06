power, compa = input("Enter Input : ").split("/")
compa = compa.split(",")
power = list(map(int, power.split()))
n = len(power)
print(sum(power))
for i in compa:
    a = int(i[0])
    b = int(i[2])
    Pa = power[a]
    Pb = power[b]

    if a*2+1 < n:
        if a*2+2 < n:
            Pa += power[a*2+2]
        Pa += power[a*2+1]
    if b*2+1 < n:
        if b*2+2 < n:
            Pb += power[b*2+2]
        Pb += power[b*2+1]
    
    if Pa > Pb: print(str(a)+">"+str(b))
    elif Pa == Pb: print(str(a)+"="+str(b))
    else: print(str(a)+"<"+str(b))



