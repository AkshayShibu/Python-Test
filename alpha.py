n=int(input())
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0,n+1):
    for j in range(0,i):
        print(alpha[j],end="")
    print()
