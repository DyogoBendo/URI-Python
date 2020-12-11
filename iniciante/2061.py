if __name__ == '__main__':
    aba_inicial, repete = map(int, input().split())
    for i in range(repete):
        acao = input()
        if acao == 'fechou':
            aba_inicial += 1
        else:
            aba_inicial -= 1
    print(aba_inicial)