if __name__ == "__main__":
    h, e, a, o, w, x = map(int, input().split())
    b = h + e + a + x
    m = o + w
    if b >= m:
        print("Middle-earth is safe.")
    else:
        print("Sauron has returned.")