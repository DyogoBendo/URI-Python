def calc_den(n):
    if n == 1:
        return 1 / 2
    else:
        return 1 / (2 + calc_den(n - 1))


if __name__ == '__main__':
    n = int(input())
    resposta = 1.0
    if n != 0:
        resposta += calc_den(n)

    print(f'{resposta:.10f}')
