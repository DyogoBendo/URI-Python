if __name__ == '__main__':
    while True:
        frase = input()
        if frase == "*":
            break
        frase = frase.lower()
        palavras = frase.split()        

        i = palavras[0][0]
        correct = True
        for p in palavras:
            if p[0] != i:
                correct = False
                break
        if correct:
            print("Y")
        else:            
            print("N")