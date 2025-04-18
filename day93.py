# cook your dish here
for _ in range (int(input())):
    n,x,y=map(int,input().split())
    r=n-1
    co=n-1
    a=min(x-1,y-1)
    b=min(x-1,n-y)
    c=min(n-x,y-1)
    d=min(n-x,n-y)
    t=r+co+a+b+c+d 
    print(t)