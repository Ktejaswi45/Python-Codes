T = int(input())

for _ in range(T):
    N = int(input())
    S = list(input().strip())
    
    # Step 1: Swap adjacent characters
    for j in range(0, N - 1, 2):
        S[j], S[j + 1] = S[j + 1], S[j]
    
    # Step 2: Replace each letter with its opposite in the alphabet
    for j in range(N):
        S[j] = chr(219 - ord(S[j]))
    
    print(''.join(S))
