if __name__ == '__main__':
    while True:
        try:
            repete = int(input())
            lesmas = input().split()
            maior = 0
            for i in range(repete):
                if int(lesmas[i]) > maior:
                    maior = int(lesmas[i])

            if maior < 10:
                print(1)
            elif 10 <= maior < 20:
                print(2)
            else:
                print(3)
        except EOFError:
            break
