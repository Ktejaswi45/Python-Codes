# cook your dish here
for _ in range (int(input())):
    x,y,d=map(int,input().split())
    if (max(x,y)-min(x,y))<=d:
        print("yes")
    else:
        print("no")