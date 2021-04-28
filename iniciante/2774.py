if __name__ == "__main__":

    while True:
        try: 
            h, m = map(int, input().split())

            qt = (h * 60) // m 

            valores = list(map(float, input().split()))

            media = sum(valores) / qt

            alfa = 0
            for i in range(qt):
                alfa += ((valores[i] - media) ** 2)
            
            sigma = (alfa / (qt - 1)) ** 0.5

            print(f'{sigma:.5f}')
        except:
            break