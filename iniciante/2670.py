if __name__ == '__main__':
    andar_1 = int(input())
    andar_2 = int(input())
    andar_3 = int(input())

    melhor_andar = 0

    # meio
    menor_tempo = andar_1 * 2 + andar_3 * 2

    # Primeiro andar
    if andar_2 * 2 + andar_3 * 4 < menor_tempo:
        menor_tempo = andar_2 * 2 + andar_3 * 4

    # ultimo andar
    if andar_1 * 4 + andar_2 * 2 < menor_tempo:
        menor_tempo = andar_1 * 4 + andar_2 * 2

    print(menor_tempo)




