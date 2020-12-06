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
    
    def clear(self):
        self.items = []
  
#---------------------------------------------------------
inp = input("Enter Input : ").split(",")
s = Stack()
for i in inp:
    #print(i)
    x = i.split()
    if x[0]=='A':
        while (not s.isEmpty()) and int(x[1])>=s.peek():
            #print(s.pop())
            s.pop()
        s.push(int(x[1]))
    elif x[0] == 'B':
        print(s.size())