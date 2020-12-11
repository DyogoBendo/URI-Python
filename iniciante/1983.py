if __name__ == '__main__':
    alunos = int(input())
    maior_nota = 8
    codigo_melhor = 'Minimum note not reached'
    for i in range(alunos):
        codigo, nota = input().split()
        nota = float(nota)
        if nota >= maior_nota:
            maior_nota = nota
            codigo_melhor = codigo
    print(codigo_melhor)