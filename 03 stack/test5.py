class Rational:
    def __init__(n,d):
        self.value = n/d
        self.str = str(n)+"/"+str(d)
    
    def __str__(self):
        return self.str
    
    def __lt__(self, value):
        if self.value < value.value:
            return True
        else:
            return False
    
    def __gt__(self, value):
        if self.value > value.value:
            return True
        else:
            return False

    def __le__(self, value):
        if self.value <= value.value:
            return True
        else:
            return False

    def __ge__(self, value):
        if self.value >= value.value:
            return True
        else:
            return False

    def __eq__(self, value):
        if self.value == value.value:
            return True
        else:
            return False

    def __ne__(self, value):
        if self.value != value.value:
            return True
        else:
            return False
    
    def __add__

    

print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")

str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]

A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational()          # C = 1/1      

print("A=",A,"B=",B)        # method __str__
print("A < B ==> ",A<B)     # method __lt__
print("A > B ==> ",A>B)     # method __gt__
print("A <= B ==> ",A<=B)   # method __ge__
print("A >= B ==> ",A>=B)   # method __gt__
print("A == B ==> ",A==B)   # method __eq__
print("A != B ==> ",A!=B)   # method __ne__
print("A + B ==> ",A+B)     # method __add__
print("A - B ==> ",A-B)     # method __sub__
print("A * B ==> ",A*B)     # method __mul__
print("A / B ==> ",A/B)     # method __truediv__
print("A // B ==> ",A//B)     # method __floordiv__
print("A + C ==> ",A+C)        