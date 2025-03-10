# cook your dish here
for _ in range (int(input())):
    n,k=map(int,input().split())
    minion_val=list(map(int,input().split()))
    t=0
    for i in minion_val:
        if (i+k)%7==0:
            t+=1
    print(t)
        