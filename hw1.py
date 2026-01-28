n=int(input())
for i in range(0,n+1):
    ch='A'
    for j in range (0,i):
        print(ch,end="")
        ch=chr(ord(ch)+1)
    print()
