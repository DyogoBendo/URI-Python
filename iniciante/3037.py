if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        x1, d1 = map(int, input().split())
        x2, d2 = map(int, input().split())
        x3, d3 = map(int, input().split())

        vj = (x1 * d1) +  (x2 * d2) + (x3 * d3)

        x1, d1 = map(int, input().split())
        x2, d2 = map(int, input().split())
        x3, d3 = map(int, input().split())

        vm = (x1 * d1) +  (x2 * d2) + (x3 * d3)

        if vj > vm:
            print("JOAO")
        else:
            print("MARIA")


