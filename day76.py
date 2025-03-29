# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = {}
    
    for i in a:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    
    max_freq = max(c.values())
    print(n - max_freq)