if __name__ == "__main__":
    i, f = map(int, input().split())

    if f - i >= 3:
        print("Muito bem! Apresenta antes do Natal!")
    elif f - i >= 0:
        print("Parece o trabalho do meu filho!")
        i += 2
        if i < 24:
            print("TCC Apresentado!")
        else:
            print("Fail! Entao eh nataaaaal!")
    else:
        print("Eu odeio a professora!")