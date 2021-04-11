def soma(a):
    return sum(a)


def media(a):
    return soma(a) / len(a)


if __name__ == '__main__':
    acao = input()
    vetor_valores_abaixo = []

    for i in range(12):
        for j in range(12):
            numero = float(input())
            if j + i > 11:
                vetor_valores_abaixo.append(numero)
    if acao == 'S':
        print(f"{soma(vetor_valores_abaixo):.1f}")
    else:
        print(f"{media(vetor_valores_abaixo):.1f}")
