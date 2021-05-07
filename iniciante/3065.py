if __name__ == "__main__":
    i = 0
    while True:
        m = int(input())
        if m == 0:
            break
        i += 1
        entrada = input()
        somas = entrada.split("+")
        r = 0
        for s in somas:
            try:
                r += int(s)
            except:
                sub = s.split("-")
                r += int(sub[0])
                r -= sum( map(int, sub[1:]))
        print("Teste", i)
        print(r)
        print()


        
