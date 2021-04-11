def verifica_troco(valor):
    num_notas = 0
    while valor >= 100 and num_notas < 2:
        valor -= 100
        num_notas += 1
    if num_notas == 1 and valor == 0:
        valor = 100
        num_notas -= 1
    while valor >= 50 and num_notas < 2:
        valor -= 50
        num_notas += 1
    if num_notas == 1 and valor == 0:
        valor = 50
        num_notas -= 1
    while valor >= 20 and num_notas < 2:
        valor -= 20
        num_notas += 1
    if num_notas == 1 and valor == 0:
        valor = 20
        num_notas -= 1
    while valor >= 10 and num_notas < 2:
        valor -= 10
        num_notas += 1
    if num_notas == 1 and valor == 0:
        valor = 10
        num_notas -= 1
    while valor >= 5 and num_notas < 2:
        valor -= 5
        num_notas += 1
    while valor >= 2 and num_notas < 2:
        valor -= 2
        num_notas += 1
    if valor == 0 and num_notas == 2:
        print('possible')
    else:
        print('impossible')


if __name__ == '__main__':
    n, m = map(int, input().split())
    while n != 0 and m != 0:
        troco = m - n
        verifica_troco(troco)
        n, m = map(int, input().split())
