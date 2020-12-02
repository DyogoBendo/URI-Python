def determina_vencedor(sheldon, raj):
    if sheldon == raj:
        return 0
    if sheldon == 'tesoura':
        if raj == 'papel' or raj == 'lagarto':
            return 1
        else:
            return 2
    if sheldon == 'papel':
        if raj == 'pedra' or raj == 'Spock':
            return 1
        else:
            return 2
    if sheldon == 'pedra':
        if raj == 'tesoura' or raj == 'lagarto':
            return 1
        else:
            return 2
    if sheldon == 'lagarto':
        if raj == 'papel' or raj == 'Spock':
            return 1
        else:
            return 2
    if sheldon == 'Spock':
        if raj == 'tesoura' or raj == 'pedra':
            return 1
        else:
            return 2


if __name__ == '__main__':
    casos = int(input())
    for i in range(casos):
        sheldon, raj = input().split()
        resultado = determina_vencedor(sheldon, raj)
        if resultado == 0:
            resposta = 'De novo!'
        elif resultado == 1:
            resposta = 'Bazinga!'
        else:
            resposta = 'Raj trapaceou!'

        print(f'Caso #{i + 1}: {resposta}')

