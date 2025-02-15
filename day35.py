# cook your dish here
for i in range(int(input())):
    w,x,y,z=map(int,input().split())
    pw= {x, y, z, x + y, x + z, y + z, x + y + z}
    if w in pw:
        print("yes")
    else:
        print("no")