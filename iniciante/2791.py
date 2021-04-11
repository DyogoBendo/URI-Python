if __name__ == "__main__":
    entrada = input().split()
    
    t = True
    for i in range(len(entrada)):
        if entrada[i] == "1":
            print(i + 1)
            t = False
    
    if t:
        print(0)