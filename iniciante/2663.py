if __name__ == '__main__':
    num_competidores = int(input())
    num_classificados = int(input())

    competidores = []
    for i in range(num_competidores):
        competidores.append(int(input()))
    competidores.sort()
    competidores.reverse()

    empatados = 0
    ultimo = competidores[num_classificados - 1]
    for i in range(num_classificados):
        if competidores[i] == ultimo:
            empatados += 1
    total_empates = competidores.count(ultimo) - empatados

    print(num_classificados + total_empates)