for _ in range(int(input())):
    s1 = input().strip()
    s2 = input().strip()
    
    min_diff = 0
    max_diff = 0
    
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if c1 == '?' or c2 == '?':
                max_diff += 1
            else:
                min_diff += 1
                max_diff += 1
        else:
            if c1 == '?' and c2 == '?':
                max_diff += 1
                
    print(min_diff, max_diff)