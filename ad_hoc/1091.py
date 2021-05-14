if __name__ == "__main__":
    while True:
        k = int(input())
        if k == 0:
            break
        d = list(map(int, input().split()))
        for i in range(k):
            leste = False
            norte = False
            c = list(map(int, input().split()))
            # 0  representa coordenada leste/oeste
            # 1 representa coordenada norte/sul

            if d[0] == c[0] or d[1] == c[1]:
                print("divisa")
            else:
                if d[0] < c[0]:
                    leste = True
                if d[1] < c[1]:
                    norte = True

                if norte and leste:
                    print("NE")
                elif norte and not leste:
                    print("NO")
                elif not norte and leste:
                    print("SE")
                else:
                    print("SO")
