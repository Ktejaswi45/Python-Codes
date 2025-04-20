for _ in range(int(input())):
    n = input()
    a = 0
    for d in n:
        a += int(d)
    parity = a % 2
    x = int(n) + 1
    while True:
        b = 0
        for d in str(x):
            b += int(d)
        if b % 2 != parity:
            print(x)
            break
        x += 1
