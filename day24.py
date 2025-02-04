# cook your dish here
for m in range(int(input())):
    X=int(input())
    if X%3==0:
        print("normal")
    elif X%3==1:
        print("huge")
    else:
        print("small")