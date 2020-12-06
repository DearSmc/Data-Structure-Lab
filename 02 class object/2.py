class Calculator:
    def __init__(self,a):
        self.a = a
    def __add__(self,x):
        return self.a + x.a
    def __sub__(self,x):
        return self.a - x.a
    def __mul__(self,x): 
        return self.a * x.a
    def __truediv__(self,x):
        return self.a / x.a

p,q = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(p)),Calculator(int(q))
print(x+y,x-y,x*y,x/y,sep = "\n")
