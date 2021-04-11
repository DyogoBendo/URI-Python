if __name__ == "__main__":
    n = int(input())
    a = 0
    e = 0
    h = 0
    m = 0
    x = 0    
    for i in range(n):
        nome, tipo = input().split()
        if tipo == "A":
            a += 1
        elif tipo == "E":
            e += 1
        elif tipo == "H":
            h += 1
        elif tipo == "M":
            m += 1
        else:
            x += 1
    print(x, "Hobbit(s)")             
    print(h, "Humano(s)")             
    print(e, "Elfo(s)")             
    print(a, "Anao(s)")             
    print(m, "Mago(s)")             