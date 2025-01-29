# cook your dish here
for i in range (int(input())):
    X,Y=map(int,input().split())
    if X%2!=0:
        if Y>=(X//2)+1:
            print("YES")
        else:
            print("NO")
    else:
        if Y>=X//2:
            print("YES")
        else:
            print("NO")