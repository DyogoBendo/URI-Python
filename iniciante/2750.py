if __name__ == '__main__':
    print("---------------------------------------")
    print("| decimal   |  octal  |  Hexadecimal  |")
    print("---------------------------------------")
    for i in range(8):
        print(f"|      {i}    |    {i}    |       {i}       |")
    for i in range(8, 10):
        octal = i + 2
        print(f"|      {i}    |   {octal}    |       {i}       |")
    hexa = ["A", "B", "C", "D", "E", "F"]
    for i in range(10, 16):
        octal = i + 2
        hexadecimal = hexa[i%10]
        print(f"|     {i}    |   {octal}    |       {hexadecimal}       |")
    print("---------------------------------------")
    print()