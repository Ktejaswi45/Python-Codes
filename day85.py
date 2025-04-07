# cook your dish here
for _ in range (int(input())):
    n,a=map(int,input().split())
    c=n-a
    print(min(c,a))