# cook your dish here
for i in range (int(input())):
    N,M=map(int,input().split())
    if (N%M)==0 and (N//M)%2==0:
        print("Yes")
    else:
        print("No")