# cook your dish here
from math import ceil
for _ in range (int(input())):
    x,y,r=map(int,input().split())
    b=round(r/30)
    c=x+b
    d=c/y
    print(ceil(d))