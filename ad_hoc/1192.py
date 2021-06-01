if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        valores = input()
        a = int(valores[0])
        b = int(valores[2])
        sinal = valores[1]

        if a == b:
            print(a * b)
        else:
            if sinal.islower():
                print(a + b)
            else:
                print(b - a)
