# cook your dish here
for x in range(int(input())):
    n=int(input())
    a=1
    for i in range (2,n+1):
        a*=i
    print(a)