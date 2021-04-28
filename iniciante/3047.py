if __name__ == "__main__":
    m = int(input())
    a = int(input())
    b = int(input())

    c = m - (a + b)

    maior = a if a > b else b
    maior = c if c > maior else maior

    print(maior)