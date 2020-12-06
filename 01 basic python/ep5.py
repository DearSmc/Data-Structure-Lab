print("Enter Input : ",end="")
n = int(input())

for i in range(n+2):
    print('.'*(n-i+1) + '#'*(i+1) + ('+'*(n+2) if(i==0 or i==n+1) else '+'+'#'*n+'+'))

for i in range(n+2):    
    print(('#'*(n+2) if(i==0 or i==n+1) else '#'+'+'*n+'#') +  '+'*(n-i+2) + '.'*(i))


'''
n = 
1 = 6 -> 3
2 = 8 -> 4
3 = 10 -> 5

'''