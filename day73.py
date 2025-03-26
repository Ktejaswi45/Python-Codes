for _ in range(int(input())):
    a, b = map(int, input().split())  
    l, bo = 0, 0  

    for i in range(1, 2000):  
        if i % 2 == 1:  
            if l + i > a:  
                print("Bob")
                break
            l += i  
        else:  
            if bo + i > b:  
                print("Limak")
                break
            bo += i  
