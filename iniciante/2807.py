if __name__ == "__main__":
    a = int(input())
    seq = [0 for _ in range(a)]
    seq [-1] = '1'
    if a >= 2:
        seq[-2] = '1'

        b = 1
        c = 1
        for i in range(a - 3, -1, -1):
            d = b + c
            b = c
            c = d

            seq[i] = str(d)            
        
    p = ' '.join(seq)
    print(p)
