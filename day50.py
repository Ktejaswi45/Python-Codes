# cook your dish here
for _ in range (int(input())):
    a,b,x,y=map(int,input().split())
    medal=0
    if a!=x and a!=y:
        medal +=1
    if b!=x and b!=y:
        medal +=1
    print(medal)