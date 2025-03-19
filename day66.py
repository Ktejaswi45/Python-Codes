# cook your dish here
for _ in range (int(input())):
    n=int(input())
    if n<=1:
        print('no')
    else:
        prime=True
        for i in range (2,int(n**0.5)+1):
            if n%i==0:
                prime=False
                break
        if prime:
            print('yes')
        else:
            print('no')