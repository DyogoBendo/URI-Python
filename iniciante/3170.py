if __name__ == "__main__":
    b = int(input())
    g = int(input())

    n = g // 2

    p = n - b 

    if p <= 0:
        print("Amelia tem todas bolinhas!")
    else:
        print(f"Faltam {p} bolinha(s)")