if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))

    maior = 0
    for i in m:
        if i > maior:
            maior = i
    maior += 1

    print(maior)
