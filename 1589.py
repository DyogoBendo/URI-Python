if __name__ == '__main__':
    repete = int(input())

    for i in range(repete):
        a, b = map(int, input().split())
        raio = a + b
        print(raio)