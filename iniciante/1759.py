if __name__ == '__main__':
    repete = int (input())
    texto = ''
    for i in range(repete):
        texto += 'Ho'
        if i == repete - 1:
            texto += '!'
        else:
            texto += ' '
    print(texto)
