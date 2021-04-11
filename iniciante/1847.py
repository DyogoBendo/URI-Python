if __name__ == '__main__':
    a, b, c = map(int, input().split())

    dif12 = b - a
    dif23 = c - b

    if dif12 < 0 <= dif23:
        print(':)')
    elif dif12 > 0 >= dif23:
        print(':(')
    elif dif12 > 0 and dif23 < dif12:
        print(':(')
    elif 0 < dif12 <= dif23:
        print(':)')
    elif dif12 < 0 and dif23 > dif12:
        print(':)')
    elif 0 > dif12 >= dif23:
        print(':(')
    elif dif12 == 0 and dif23 > dif12:
        print(':)')
    elif dif12 == 0 and dif23 <= dif12:
        print(':(')
