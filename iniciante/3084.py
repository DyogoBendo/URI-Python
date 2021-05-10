if __name__ == "__main__":
    while True:
        try:
            h, m = map(int, input().split())
            h //= 30
            m //= 6
            
            hs = str(h) if h > 9 else '0'+str(h)
            ms = str(m) if m > 9 else '0'+str(m)

            print(f'{hs}:{ms}')
            
        except:
            break