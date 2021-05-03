if __name__ == "__main__":
    n = int(input())
    i = 0    

    a = 2
    b = 3    
    while i < n:
        c = a + b
        a = b
        b = c

        for j in range(a + 1, b):
            fibonot = j
            i += 1

            if i == n:
                break
    
    print(fibonot)

