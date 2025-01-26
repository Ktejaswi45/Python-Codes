# cook your dish here

N= int(input())
A=list(map(int,input().split()))
temp=0
for i in A:
    if i%2==0:
        temp=temp+1
if temp>N-temp:
    print("READY FOR BATTLE")
else:
    print("NOT READY")