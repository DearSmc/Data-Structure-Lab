class Stack:
    
    def __init__(self,Lis = None):
        if Lis == None:
            self.items = [] 
        else:
            self.items = Lis

    def push(self,data):
        self.items.append(data)
    
    def pop(self,index =  None):
        if index == None:
            return self.items.pop()
        else:
            return self.items.pop(index)
    
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

    def indexOf(self,data):
        for i in range(self.size()):
            if self.items[i]==data:
                return i
        return -1

#------------------------------------------------------------------------------------------------

inp = input("******** Parking Lot ********\nEnter max of car,car in soi,operation : ").split()
s = Stack()

if inp[1]!='0':
    x = inp[1].split(",")
    for i in x:
       # print("3")
        s.push(int(i))

if inp[2]=="arrive":
  #  print("1")
    if s.size()<int(inp[0]):
        if not (int(inp[3]) in s.get()):        
            s.push(int(inp[3]))
            print("car "+inp[3]+" arrive! : Add Car "+inp[3])
        else:
            print("car {} already in soi".format(inp[3]))
    else:
        print("car {} cannot arrive : Soi Full".format(inp[3]))
elif inp[2]=="depart":
   # print("2")
    if s.size()>0:
        if int(inp[3]) in s.get():
            if s.indexOf(int(inp[3])) != -1:
      #          print("pop"+str(s.indexOf(int(inp[3]))))
                s.pop(s.indexOf(int(inp[3])))
                print("car {} depart ! : Car {} was remove".format(inp[3],inp[3]))
        else:
            print("car {} cannot depart : Dont Have Car {}".format(inp[3],inp[3]))
    else:
        print("car {} cannot depart : Soi Empty".format(inp[3]))

print(s.get())