# cook your dish here
for _ in range (int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    l=0
    for i in range (n):
        temp=abs(a[i]-1)
        tem=abs(a[i]-m)
        l+=max(temp,tem)
        
    print(l)