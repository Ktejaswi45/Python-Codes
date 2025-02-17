# cook your dish here
for i in range (int(input())):
    n,a,b=map(int,input().split())
    t=a*(n//2)+b*(n-n//2)
    print(t)