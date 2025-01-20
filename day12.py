# ATM machine code
T= int(input())
for i in range(T):
    N,K=map(int,input().split())
    W=list(map(int,input().split()))
    result = ""
    for j in W:
        if K>=j:
            result += "1"
            K -= j
        
        else:
            result += "0"
            
    print(result)
        