# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    ft=x*y
    if x%3==0:
        gap_time=(x//3)-1
    else:
        gap_time=(x//3)
    total=ft+gap_time*z
    print(total)
        