# cook your dish here
for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if (a-y)<=b<=(a+x):
        print("yes")
    else:
        print("no")