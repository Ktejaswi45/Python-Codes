# cook your dish here
for _ in range (int(input())):
    a,b,x,y=map(int,input().split())
    c=a/x
    d=b/y
    if c<d:
        print("chef")
    elif c>d:
        print("chefina")
    else:
        print("both")