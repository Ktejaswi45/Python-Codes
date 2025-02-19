# cook your dish here
for i in range (int(input())):
    x,n=map(int,input().split())
    a=round(n/100)
    if a>x:
        if (n%100)==0:
            print((n//100)-x)
        else:
            print(((n//100)-x)+1)
    else:
        print(0)