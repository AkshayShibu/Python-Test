n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n-i+2):
        print("*",end="")
    for s in range(1,n+1-i):
        print("*",end="")
    print()