inp = input("Enter Input : ").split(",")
a=[]
b=[]
for i in range(len(inp)):
   x = inp[i].split()
   a.append(int(x[0]))
   b.append(int(x[1]))

output = []
output.append(b[0])
i=1
temp = []
temp.append(a[0])

while i<len(a):
   if a[i] <= temp[-1]:
      output.append(b[i]) 
      temp.append(a[i])  
   else:
      while len(temp)>0 and a[i]>temp[-1]:
         print(output.pop())
         temp.pop()
      temp.append(a[i])
      output.append(b[i])   
   i+=1
   
