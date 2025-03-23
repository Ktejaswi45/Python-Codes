# cook your dish here
for _ in range (int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    for i in range (n):
        s+=a[i] 
        if s<k:
            print('no',i+1)
            break
        s-=k
    else:
        print('yes')