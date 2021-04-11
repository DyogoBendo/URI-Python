def calcula_primo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True
    for i in range(2, 10000):
        if numero % i == 0 and i != numero:
            return False
    return True


if __name__ == '__main__':
    while True:
        try:
            M = int(input())
            moedas = []
            for i in range(M):
                moedas.append(int(input()))
            n = int(input())
            soma = 0
            for i in range(M - 1, -1, - n):
                soma += moedas[i]
            is_primo = calcula_primo(soma)
            if is_primo:
                print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
            else:
                print('Bad boy! I’ll hit you.')
        except EOFError:
            break