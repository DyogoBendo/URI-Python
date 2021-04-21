if __name__ == "__main__":
    n = int (input())
    m = int(input())
    lista = set()
    for i in range(m):
        lista.add(int(input()))
    
    print(n - len(lista))
