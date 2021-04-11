if __name__ == '__main__':
    repete = int(input())
    saques_tot = 0
    bloqueios_tot = 0
    ataque_tot = 0

    saques_acert = 0
    bloqueios_acert = 0
    ataque_acert = 0
    for i in range(repete):
        nome = input()
        saques_tent, bloqueios_tent, ataque_tent = map(int, input().split())
        saques_tot += saques_tent
        ataque_tot += ataque_tent
        bloqueios_tot += bloqueios_tent
        saques, bloqueios, ataque = map(int, input().split())
        saques_acert += saques
        bloqueios_acert += bloqueios
        ataque_acert += ataque

    rs = (saques_acert / saques_tot) * 100
    rb = (bloqueios_acert / bloqueios_tot) * 100
    ra = (ataque_acert / ataque_tot) * 100
    print(f'Pontos de Saque: {rs:.2f} %.\nPontos de Bloqueio: {rb:.2f} %.\nPontos de Ataque: {ra:.2f} %.')
