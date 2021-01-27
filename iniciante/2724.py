if __name__ == '__main__':
    testes = int(input())
    for i in range(testes):
        perigoso = []
        compostos = []
        t = int(input())
        for j in range(t):
            perigoso.append(input())
        u = int(input())
        for j in range(u):
            compostos.append(input())
        for j in compostos:
            problema = False
            for k in perigoso:
                if j.find(k) > -1:
                    print('Abortar')
                    problema == True
                    break
            if not problema:
                print('Prossiga')

        print()


