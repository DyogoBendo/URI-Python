def define_onda(valores):
    for i in range(1, len(valores)):
        anterior = valores[i - 1]
        atual = valores[i]

        if atual == anterior:
            return 0

        if atual < anterior:
            sou_vale = True
        elif atual > anterior:
            sou_vale = False
        if i == 1:
            vale_anterior = not sou_vale

        if sou_vale == vale_anterior:
            return 0

        vale_anterior = sou_vale

    return 1


if __name__ == '__main__':
    repete = int(input())
    valores = list(map(int, input().split()))
    print(define_onda(valores))
