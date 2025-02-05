# cook your dish here
for i in range (int(input())):
    X,Y,Z=map(int,input().split())
    a=max(0,(Z-(Y//X)))
    print(a)