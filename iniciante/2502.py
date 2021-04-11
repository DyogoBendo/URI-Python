if __name__ == '__main__':
    while True:
        try:
            tamanho, num_frases = map(int, input().split())
            troca1 = input()
            troca2 = input()
            teve = 0

            for i in range(num_frases):
                frase = input()
                resultado = ''
                for j in range(tamanho):
                    letra1 = troca1[j]
                    letra2 = troca2[j]
                    for k in range(len(frase)):
                        if frase[k] == letra1:
                            if not letra1.isalpha():
                                resultado += letra2.lower()
                            else:
                                resultado += letra2
                        elif frase[k] == letra2:
                            if not letra2.isalpha():
                                resultado += letra1.lower()
                            else:
                                resultado += letra1
                        elif frase[k] == letra1.lower():
                            resultado += letra2.lower()
                        elif frase[k] == letra2.lower():
                            resultado += letra1.lower()
                        else:
                            resultado += frase[k]
                    frase = resultado
                    resultado = ''
                print(frase)
            print()
        except:
            break
