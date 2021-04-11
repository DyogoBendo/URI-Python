if __name__ == '__main__':
    entrada = input()
    num_1 = entrada.count('1')
    if num_1 % 2 == 0:
        print(f'{entrada}0')
    else:
        print(f'{entrada}1')