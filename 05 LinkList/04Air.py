class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.mark=None

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,i):
        newNode=Node(i)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def size(self):
        # print('enter size function')
        cur=self.head
        if cur==None:
            return 0
        else:
            s=1
            while cur.next!=None:
                # print('enter while loop')
                s+=1
                cur=cur.next
            return s
    def getPointerAtIndex(self,index):
        if int(index) < self.size() and int(index)>-1:
            cur=self.head
            print("*****************")
            for i in range(0,int(index)):
                print(i)
                cur=cur.next
            return cur
        else:
            return "not have index"
            
    def getMemberLinklist(self):
        if self.head==None:
            return "Empty"
        else:
            s=""
            cur=self.head
            while cur.next!=None:
                s+=cur.data
                s+="->"
                cur=cur.next
            s+=str(cur.data)
            return s
    def checkLoop(self):
        # print('begining of the function')
        if self.head!=None:
            # print('enter else case')
            cur=self.head
            while cur.next!=None:
                # print('in while loop')
                if cur.mark==None and cur.next!=None:
                    cur.mark="*"
                    cur=cur.next
                elif cur.mark==None and cur.next==None:
                    return "not Loop"
                else:
                    return "Loop"
                    
            if cur.mark==None:
                return "not Loop"
            else:
                return "Loop"
        else:
            return "not Loop"
        
            

x=input("Enter input : ").split(",")
lis=[]
link=LinkList()
for i in x:
    lis.append(i.split(" "))
#print(lis)
for j in lis:
    if j[0]=="A":
        link.append(j[1])
        print(link.getMemberLinklist())
    elif j[0]=="S":
        if link.size()==0:
            print("Error! {list is empty}")
        elif int(j[1][0])>=link.size():
            print("Error! {index not in length}: "+j[1][0])
        elif int(j[1][2])>=link.size():
            link.append(int(j[1][2]))
            print("index not in length, append : "+j[1][2])
        else:
            print("Set node.next complete!, index:value = "+j[1][0]+":"+link.getPointerAtIndex(j[1][0]).data+" -> "+j[1][2]+":"+link.getPointerAtIndex(j[1][2]).data)
            cur  = link.getPointerAtIndex(j[1][0])
            # print(link.getPointerAtIndex(j[1][0]))
            cur1 = link.getPointerAtIndex(j[1][2])
            # print(link.getPointerAtIndex(j[1][2]))
            cur.next=cur1
            
    
if link.checkLoop()=="not Loop":
    print("No Loop")
    print(link.getMemberLinklist())
else:
    print("Found Loop")
