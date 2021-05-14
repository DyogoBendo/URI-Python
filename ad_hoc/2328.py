if __name__ == '__main__':
    n = int(input())
    lista = list(map(int, input().split()))
    print(sum(lista) - n)