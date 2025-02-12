# cook your dish here
for i in range (int(input())):
    a,b,c,d=map(int,input().split())
    e=abs(a-c)
    f=abs(b-d)
    g=max(e,f)
    print(g)