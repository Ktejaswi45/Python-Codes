# cook your dish here
for i in range (int(input())):
    s,x,y,z=map(int,input().split())
    m=s-(x+y)
    ml=z-m
    if ml<=0:
        print(0)
    elif ml<=(max(x,y)):
        print(1)
    else:
        print(2)