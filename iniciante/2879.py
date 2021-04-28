if __name__ == "__main__":
    n = int(input())

    w = 0
    for i in range(n):
        p = int(input())

        if p != 1:
            w += 1
    
    print(w)