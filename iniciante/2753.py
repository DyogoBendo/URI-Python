import string
if __name__ == "__main__":
    a = string.ascii_lowercase
    b = 97
    for i in range(len(a)):        
        print(b, 'e', a[i])
        b += 1