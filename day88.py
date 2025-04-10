T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            break

    ok = True
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            ok = False
            break

    print("YES" if ok else "NO")
