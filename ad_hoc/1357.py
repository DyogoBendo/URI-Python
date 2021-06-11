if __name__ == '__main__':
    numbers = [".*\n**\n.." ,"*.\n..\n..", "*.\n*.\n..", "**\n..\n..", "**\n.*\n..", "*.\n.*\n..", "**\n*.\n..", "**\n**\n..", "*.\n**\n..", ".*\n*.\n.."]

    while True:
        n = int(input())
        if n == 0:
            break
        d = input()
        if d == "S":
            v = input()
            for c in v:
                print(numbers[int(c)], end='')                        
        else:
            v = [""] * n
            for i in range(3):
                v[i] += input() + '\n'
            for c in v:
                print(numbers.index(c), end='')


