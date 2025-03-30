# cook your dish here
for _ in range (int(input())):
    n=int(input())
    s=input().strip()
    t={}
    for i in (s):
        t[i]=t.get(i,0)+1
    if all(i % 2 == 0 for i in t.values()):
        print("yes")
    else:
        print("no")