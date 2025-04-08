# cook your dish here
for _ in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    temp=0
    sum=0
    for i in (a):
        sum+=i
        if i%2!=0:
            temp+=1
    if temp>=2 and sum%2==0:
        print("yes")
    else:
        print("no")