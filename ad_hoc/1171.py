def get_items(x):
    y = int(x[0])
    z = (y, x[1])
    return z

if __name__ == '__main__':
    n = int(input())

    numeros = {}
    for _ in range(n):
        numero = input()
        try:
            numeros[numero] += 1
        except:
            numeros[numero] = 1
    
    chaves = list(map(get_items, numeros.items()))  
    chaves.sort()    
    for k, v in chaves:
        print(f'{k} aparece {v} vez(es)')