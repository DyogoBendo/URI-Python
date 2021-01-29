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
                b = j.count(k)
                while b > 0:
                    print(b)
                    b -= 1
                    a = j.find(k)
                    if a + len(k) < len(j) - 1:
                        a += len(k)
                        if 'z' >= j[a] >= 'a' or '0' < j[a] <= '9':
                            j = j[a:]
                            a = j.find(k)
                            problema is False
                            continue
                        else:
                            print(j)
                            print('Abortar')
                            problema is True
                            break
                    else:
                        print(j)
                        print('Abortar')
                        problema is True
                        break
                if problema:
                    break
            if not problema:
                print(j)
                print('Prossiga')

        print()


