if __name__ == '__main__':
    while True:
        try:
            dodo, leo, pep = input().split()
            if dodo != leo != pep != dodo:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif dodo == leo == pep:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif dodo == 'papel':
                if dodo == leo:
                    if pep == 'pedra':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif pep == 'tesoura':
                        print('Urano perdeu algo muito precioso...')
                elif dodo == pep:
                    if leo == 'pedra':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif leo == 'tesoura':
                        print("Iron Maiden's gonna get you, no matter how far!")
                elif pep == leo:
                    if pep == 'pedra':
                        print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                    else:
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif dodo == 'tesoura':
                if dodo == leo:
                    if pep == 'papel':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif pep == 'pedra':
                        print('Urano perdeu algo muito precioso...')
                elif dodo == pep:
                    if leo == 'papel':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif leo == 'pedra':
                        print("Iron Maiden's gonna get you, no matter how far!")
                elif pep == leo:
                    if pep == 'papel':
                        print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                    else:
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif dodo == 'pedra':
                if dodo == leo:
                    if pep == 'tesoura':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif pep == 'papel':
                        print('Urano perdeu algo muito precioso...')
                elif dodo == pep:
                    if leo == 'tesoura':
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
                    elif leo == 'papel':
                        print("Iron Maiden's gonna get you, no matter how far!")
                elif pep == leo:
                    if pep == 'tesoura':
                        print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
                    else:
                        print('Putz vei, o Leo ta demorando muito pra jogar...')
        except EOFError:
            break