if __name__ == "__main__":
    a, b, c = input().split('/')
    print(f'{b}/{a}/{c}')
    print(f'{c}/{b}/{a}')
    print(f'{a}-{b}-{c}')