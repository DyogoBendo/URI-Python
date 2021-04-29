if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        lista = list(map(int, input().split()))

        lista_impares = [ l for l in lista if l % 2 != 0]

        lista_impares.sort()  # ordenada em ordem crescente 

        lista_final = []
        j = 0
        k = len(lista_impares) - 1
        while j <= k:
            if len(lista_final) % 2 != 0:
                lista_final.append(str(lista_impares[j]))
                j += 1
            else:
                lista_final.append(str(lista_impares[k]))
                k -= 1

        r = ' '.join(lista_final)
        print(r)
        
