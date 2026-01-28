n=int(input())
for i in range(1,n):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        if i==i or i==n or j==1 or j==n:
            print("*",end="") 
        else:
            print(" ",end="") 
    for s in range(0,i-1):
        if i==i or i==n or j==1 or j==n:
            print("*",end="")
        
    print()

for i in range(1,n+1):
    for j in range(1,i+1-1):
        print(" ",end="")
    for k in range(1,n-i+2):

        print("*",end="")
    for s in range(1,n+1-i):
        print("*",end="")
    print()