# cook your dish here
from math import ceil
for _ in range (int(input())):
    h,x,y=map(int,input().split())
    a=(h-y)/x
    print(ceil(a)+1)