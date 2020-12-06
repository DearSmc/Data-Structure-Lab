class Stack:
    
    def __init__(self,name=None):
        
        self.items = []
        self.name = name

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
            return self.items[self.size()-1]
        elif 0 <= oder < self.size() or oder >= -self.size():
            return self.items[oder]
        else:
            return -1
        # else:
            # return self.items[oder]
        

    def size(self):
        return len(self.items)

    def __str__(self):
        
        return " ".join(map(str,self.items))
    
    def clear(self):
        self.items = []
    
    def getName(self):
        return self.name

def move(n,start,end,buf):
    if n==0:
        return
    else:
        move(n-1,start,buf,end)
        
        temp = start.peek()
        end.push(start.pop())
        print("move",temp,"from ",start.getName(),"to",end.getName())
        printStack()
        
        move(n-1,buf,end,start)

def printStack():
    maxN = max(a.size(),b.size(),c.size())
    # print(maxN)
    # 5-i <= 4

    # n = 4
    # maxN    i   bool
    # 4       0   f
    # 4       1   t
    # 4       2   t
    # 4       3   t   
    # 4       4   t
    
    # 3       0   f
    # 3       1   f
    # 3       2   t
    # 3       3   t   
    # 3       4   t
    # if i >= n+1-maxN 
    # ทำ maxN ครังจากหลัง
    curA = -1
    curB = -1
    curC = -1
    for i in range(n+1):
        if i >= n+1-maxN:
            if i >= n+1-a.size():
                print(str(a.peek(curA)),end="  ")
                curA -= 1
            else:
                print("|",end="  ")
            if i >= n+1-b.size():
                print(str(b.peek(curB)),end="  ")
                curB -= 1
            else:
                print("|",end="  ")
            if i >= n+1-c.size():
                print(str(c.peek(curC)))
                curC -= 1
            else:
                print("|")
        
        else:
            print("|  |  |")
        

n = int(input("Enter Input : "))
a,b,c = Stack("A"),Stack("B"),Stack("C")
for i in range(n):
    a.push(n-i)
printStack()
move(n,a,c,b)
