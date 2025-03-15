# cook your dish here
import math
for _ in range (int(input())):
    n,a,b=map(int,input().split())
    rou=int(math.log2(n))
    tot=(rou*a)+((rou-1)*b)
    print(tot)