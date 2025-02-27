# cook your dish here
for _ in range (int(input())):
    n,x,p=map(int,input().split())
    a=n-x
    if (x*3)-a>=p:
        print("pass")
    else:
        print("fail")