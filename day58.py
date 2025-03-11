# cook your dish here
from math import ceil
for _ in range (int(input())):
    a,b,k=map(int,input().split())
    if a==b:
        print(0)
    else:
        c=abs(a-b)/k
        print(ceil(c))