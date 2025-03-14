# cook your dish here
for i in range (int(input())):
    A1,A2,A3,B1,B2,B3=map(int,input().split())
    A=(A1,A2,A3)
    c=sorted(A)
    sum_A=c[-1]+c[-2]
    B=(B1,B2,B3)
    d=sorted(B)
    sum_B=d[-1]+d[-2]
    if sum_A>sum_B:
        print("Alice")
    elif sum_A<sum_B:
        print("Bob")
    else:
        print("Tie")