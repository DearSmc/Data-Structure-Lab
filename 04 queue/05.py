nor,mir = input("Enter Input (Normal, Mirror) : ").split()

nor = list(nor)
mir = list(mir)
# print(nor,mir)
lst = []
i = 0
mir = list(reversed(mir))
while i < len(mir)-2:
    if mir[i]==mir[i+1]==mir[i+2]:
        lst.append(mir[i])
        # print(mir[i])
        mir.pop(i)
        mir.pop(i)
        mir.pop(i)
        i=0
        continue
    i+=1
    
mir = list(reversed(mir))


# print("mir :",end="")
# print(mir,len(mir))
# print("lst :",end="")
# print(lst)

n= len(lst)
i = 0
interup = False
complate = 0
fail = 0 
while i < len(nor)-2:
    if nor[i]==nor[i+1]==nor[i+2]:
        if len(lst)>0:
            interup = True
            nor.insert(i+2,lst.pop(0))
        # print(nor[i],nor[i+1],nor[i+2],fail,complate)
        if nor[i]==nor[i+1]==nor[i+2]:
            if interup:
                fail+=1
            else:
                complate+=1
            # print(nor[i],nor[i+1],nor[i+2],fail,complate)
            nor.pop(i)
            nor.pop(i)
            nor.pop(i)
            interup=False
            i=0
            continue
        interup=False
    i+=1

# print(nor,fail,complate)

print("NORMAL :\n"+str(len(nor)))

if len(nor)>0:
    print("".join(list(reversed(nor))))
else:
    print("Empty")
    
print("{} Explosive(s) ! ! ! (NORMAL)".format(complate))

if fail:
    print("Failed Interrupted {} Bomb(s)".format(fail))

print("------------MIRROR------------\n: RORRIM")
print(len(mir))
if len(mir)>0:
    print("".join(mir))
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(n))
        
