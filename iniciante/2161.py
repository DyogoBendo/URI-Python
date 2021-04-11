def calc_den(n):
    if n == 1:
        return 1 / 6
    else:
        return 1 / (6 + calc_den(n - 1))


n = int(input())
resposta = 3.0
if n != 0:
    resposta += calc_den(n)

print(f'{resposta:.10f}')
