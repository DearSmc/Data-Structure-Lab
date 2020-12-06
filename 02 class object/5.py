class Email:
    def __init__(self):
        self.first = None
        self.last = None
        self.fullname = None
    
    def setName(self,first,last):
        self.setFirst(first)
        self.setLast(last)
        self.fullname = self.first+" "+self.last
    def setFirst(self,first):
        self.first = first.capitalize()
    def setLast(self,last):
        self.last = last.capitalize()

    def getName(self):
        res = " -> Fullname : "
        if self.first:
            if self.last:
                self.fullname = self.first + " " + self.last
                res += self.fullname
            else: 
                res += "Please Enter Your Lastname"
        else:
            if self.last:
                res += "Please Enter Your Firstname"
            else:
                res += "Please Enter Your Firstname & Lastname"
        return res
        
    def getFirst(self):
        res = " -> Firstname : "
        if self.first:
            res += self.first
        else:    
            res += "Please Enter Your Firstname"
        return res

    def getLast(self):
        res = " -> Lastname : "
        if self.last:
            res += self.last
        else:    
            res += "Please Enter Your Lastname"
        return res
        
    def getMail(self):
        res = " -> Email : "
        if self.first:
            if self.last:
                res += self.first.lower()+"."+self.last.lower()+"@kmitl.ac.th"
            else: 
                res += "Please Enter Your Lastname"
        else:
            if self.last:
                res += "Please Enter Your Firstname"
            else:
                res += "Please Enter Your Firstname & Lastname"
        return res
      
    
inp = list((input("*** Create Email < BY KMITL > ***\nEnter Input : ").strip().split(",")))

 
a = Email()

for i in inp:
    if( i[0] == 'E'):
        print("'E'"+a.getMail())
    elif(i[0] == 'A'):
        x = i.split()
        a.setName(x[1],x[2])
    elif(i[0] == 'F'):
        x = i.split()
        a.setFirst(x[1])
    elif(i[0] == 'L'):
        x = i.split()
        a.setLast(x[1])
    elif(i == 'SA'):    
        print("'SA'"+a.getName())
    elif(i == 'SF'):
        print("'SF'"+a.getFirst())
    elif(i == 'SL'):
        print("'SL'"+a.getLast())
    elif(i == 'X'):
        break
    else:
        print("\'" +i+ "\'"+" is Invalid Input !!!")
        break



        

