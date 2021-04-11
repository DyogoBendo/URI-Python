if __name__ == "__main__":
    a = str(int(input()))
    b = str(int(input()))
    c = str(int(input()))
    
    inicio_a = a[0] if a[0] == "-" else ""
    inicio_b = b[0] if b[0] == "-" else ""
    inicio_c = c[0] if c[0] == "-" else ""
     
    print(f'A = {a}, B = {b}, C = {c}')
    print(f'A = {a.rjust(10)}, B = {b.rjust(10)}, C = {c.rjust(10)}')
    print(f'A = {inicio_a}{a[len(inicio_a):len(a)].rjust(10 - len(inicio_a), "0")}, B = {inicio_b}{b[len(inicio_b):len(b)].rjust(10 - len(inicio_b), "0")}, C = {inicio_c}{c[len(inicio_c):len(c)].rjust(10 - len(inicio_c), "0")}')
    print(f'A = {a.ljust(10)}, B = {b.ljust(10)}, C = {c.ljust(10)}')