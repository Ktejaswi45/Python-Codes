# cook your dish here

T=int(input())
for i in range(T):
    X1,X2,X3=map(int,input().split())
    Y1,Y2,Y3=map(int,input().split())
    Dt=X1+X2+X3
    St=Y3+Y2+Y1
    
    if Dt>St:
        print("DRAGON")
    elif Dt<St:
        print("SLOTH")
        
    elif Dt==St:
        if X1>Y1:
            print('DRAGON')
        elif X1<Y1:
            print('SLOTH')
        else:
            if X2>Y2:
                print("DRAGON")
            elif X2<Y2:
                print("SLOTH")
            else:
                print("TIE")