if __name__ == "__main__":
    while True:
        try:
            ano = int(input())

            middle = 1 if ano % 100 != 0 else 0
            seculo = ano // 100 + middle

            print(seculo)

        except:
            break