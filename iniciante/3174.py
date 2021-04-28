if __name__ == "__main__":
    n = int(input())

    p = 0

    horas = {
        "bonecos": 0,
        "arquitetos": 0,
        "musicos": 0,
        "desenhistas": 0,
    }    

    for i in range(n):
        nome, t, h = input().split()
        h = int(h)
        horas[t] += h
    
    p += horas["bonecos"] // 8
    p += horas["arquitetos"] // 4
    p += horas["musicos"] // 6
    p += horas["desenhistas"] // 12

    print(p)
    
        