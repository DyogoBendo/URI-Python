if __name__ == "__main__":
    while True:
        try:

            cases = {
                "esquerda": "ingles",
                "direita": "frances",
                "nenhuma": "portugues",
                "as duas": "caiu"
            }

            caso = input()

            print(cases[caso])
        except:
            break