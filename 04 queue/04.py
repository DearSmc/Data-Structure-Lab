inp = input("Enter Input : ").split(",")
# print(inp)
activity = ["Eat","Game","Learn","Movie"]
Location = ["Res.","ClassR.","SuperM.","Home"]
me=[]
you=[]
myAct=[]
yourAct=[]
score = 0
for i in inp:
    me.append(i.split()[0])
    you.append(i.split()[1])
# print(me)
# print(you)
print("My   Queue = "+", ".join(me))
print("Your Queue = "+", ".join(you))

for i in me:
    myAct.append(activity[int(i[0])]+":"+Location[int(i[2])])
print("My   Activity:Location = "+", ".join(myAct))

for i in you:
    yourAct.append(activity[int(i[0])]+":"+Location[int(i[2])])
print("Your Activity:Location = "+", ".join(yourAct))

for i in range(0,len(me)):
    if me[i]==you[i]:
        score += 4
    elif me[i][0]==you[i][0]:
        score += 1
    elif me[i][2]==you[i][2]:
        score += 2
    else:
        score -= 5 

if score>=7:
    print("Yes! You're my love! : Score is "+str(score)+'.')
elif score>0:
    print("Umm.. It's complicated relationship! : Score is "+str(score)+'.')
else:
    print("No! We're just friends. : Score is "+str(score)+'.')