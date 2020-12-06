class Stack:
    
    def __init__(self,Lis = None):
        if Lis == None:
            self.items = [] 
        else:
            self.items = Lis

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def peek(self,oder = None):
        if oder == None:
            return self.items[-1]
        else:
            return self.items[oder]
    
    def size(self):
        return len(self.items)

    def get(self):
        return self.items
        

inp = input("Enter Input : ").split()

s = Stack()
s.push(inp[0])
combo = 0
count = 1

for i in range(1,len(inp)):
    if inp[i]==s.peek():
        count+=1
        if count ==3:
            s.pop()
            s.pop()
            combo +=1
            count = 1
        else:
            if s.size() >= 2 and inp[i]==s.peek(-2):
                s.pop()
                s.pop()
                combo +=1
                count = 1
            else: 
                s.push(inp[i])
    else:
        count=1
        s.push(inp[i])

print(s.size())
if s.size():
    for i in s.get()[::-1]:
        print(i,end="")
    print("")
else:
    print("Empty")

if combo>1:
    print("Combo : "+str(combo)+" ! ! !")