if __name__ == '__main__':
    repete = int(input())
    for i in range(repete):
        nome = input()
        dificuldade = float(input())
        notas = list(map(float, input().split()))
        notas.sort()
        notas.pop(-1)
        notas.pop(0)
        print(f'{nome} {sum(notas) * dificuldade:.2f}')