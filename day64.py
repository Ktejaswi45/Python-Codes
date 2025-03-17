# cook your dish here
for _ in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range (n):
        if a[i]!=0:
            ans=i 
    print(ans)