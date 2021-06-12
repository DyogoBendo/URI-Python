if __name__ == '__main__':
    numbers = [ [".*", "*.", "*.", "**", "**", "*.", "**", "**", "*.", ".*"], ["**", "..", "*.", "..", ".*", ".*", "*.", "**", "**", "*."], ["..", "..", "..", "..", "..", "..", "..", "..", "..", ".."]]
    numbers2 = [".* \n** \n.." ,"*. \n.. \n..", "*. \n*. \n..", "** \n.. \n..", "** \n.* \n..", "*. \n. *\n..", "** \n*. \n..", "** \n** \n..", "*. \n** \n..", ".* \n*. \n.."]


    while True:
        n = int(input())
        if n == 0:
            break
        d = input()
        if d == "S":
            v = input()
            for i in range(3):
                for c in v:
                    print(numbers[i][int(c)], end="")
                print()
        else:
            v = [""] * n
            for i in range(3):
                v[i] += input() + "\n"
            for c in v:
                print(numbers2.index(c), end='')


