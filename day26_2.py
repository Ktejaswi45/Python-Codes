# cook your dish here
for _ in range (int(input())):
    N=int(input())
    S=input().strip()
    temp = ""
    for i in (S):
        if i=="A":
            temp +="T"
        elif i=="T":
            temp+="A" 
        elif i=="G":
            temp+="C"
        else:
            temp+="G"
    print(temp)