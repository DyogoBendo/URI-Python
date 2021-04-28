def check_valid(s):    
    if len(s) > 3:
        return False
    if len(s) < 3:        
        return True
    
    if s[0] > "X":
        return False
    if s[0] == "X":
        if s[1] > "F":
            return False
        if s[1] == "F":
            if s[2] > "D":
                return False
    
    return True


if __name__ == "__main__":    
    BASE_VALUE = ord('A') - 1

    while True:      
        try:   
            col = input()                        

            if len(col) < 1 or len(col) > 10:
                break
            

            if not check_valid(col):
                print("Essa coluna nao existe Tobias!")
            else:            
                r = 0
                m = 1
                for i in range(len(col) - 1, -1, -1):
                    caracter = ord(col[i]) - BASE_VALUE
                    r += (caracter * m)
                    m *= 26
                print(r)            
        except:
            break
        