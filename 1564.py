def vai_ter_copa(reclamacao):
    if reclamacao == 0:
        return 'vai ter copa!'
    return 'vai ter duas!'


if __name__ == '__main__':
    while True:
        try:
            reclamacao = int(input())
            print(vai_ter_copa(reclamacao))
        except EOFError:
            break
