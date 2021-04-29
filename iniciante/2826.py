if __name__ == "__main__":
    a = input()
    b = input()

    end = len(a) if len(b) > len(a) else len(b)

    i = 0    

    if len(a) > len(b):
        menor = b
        maior = a
    else:
        menor = a
        maior = b

    while i < end:
        if a[i] < b[i]:
            menor = a
            maior = b
            break
        elif a[i] > b[i]:
            menor = b
            maior = a
            break
        else:            
            i += 1

    print(menor)
    print(maior)