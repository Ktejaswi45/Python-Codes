# cook your dish here
for _ in range (int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    i1=p.index(1)
    i=p.index(n)
    fm=i1
    bm=(n-1)-i
    tot=fm+bm
    if i1>i:
        tot -=1 
    print(tot)