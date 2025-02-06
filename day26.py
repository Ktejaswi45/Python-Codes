# cook your dish here
for _ in range (int(input())):
    x,y=map(int,input().split())
    a=((y-x)//8)
    if x>=y:
        print(0)
    elif (y-x)%8==0:
        print(a)
    else:
        print(a+1)
        