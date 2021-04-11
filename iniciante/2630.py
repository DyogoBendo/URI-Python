if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        conversao = input()
        r, g, b = map(int, input().split())
        if conversao == 'eye':
            resultado = int(r * 0.30 + g * 0.59 + b * 0.11)
            print(f'Caso #{i + 1}: {resultado}')
        elif conversao == 'mean':
            resultado = int((r + b + g) / 3)
            print(f'Caso #{i + 1}: {resultado}')
        elif conversao == 'max':
            grupo = [r, g, b]
            grupo.sort()
            grupo.reverse()
            resultado = grupo[0]
            print(f'Caso #{i + 1}: {resultado}')
        else:
            grupo = [r, g, b]
            grupo.sort()
            resultado = grupo[0]
            print(f'Caso #{i + 1}: {resultado}')