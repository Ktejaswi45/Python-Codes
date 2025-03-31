# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    o=s.count('1')
    z=n-o
    print(min(o,z+1))