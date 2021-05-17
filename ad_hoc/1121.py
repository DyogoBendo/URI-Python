def check_movement(l, c):
    global arena, n, m, f
    if l >= n or l < 0 or c >= m or c < 0:
        return False
    elif arena[l][c] == "#": 
        return False
    elif arena[line][column] == "*":
        arena[line][column] = '.'
        f += 1
    return True

if __name__ == '__main__':
    turn_right = {
        "N": "L",
        "L": "S",
        "S": "O",
        "O": "N"
    }
    turn_left = {
        "N": "O",
        "L": "N",
        "S": "L",
        "O": "S"
    }    

    while True:        
        n, m, s = map(int, input().split())   # numero linhas, colunas e instruções
        if m == n == s == 0:
            break        
        arena = []
        pi = []
        f = 0
        directions = ("N", "S", "L", "O")
        for i in range(n):
            linha = input()                 
            for d in directions:
                if d in linha:
                    pi = [i, linha.find(d), d]                        
                    break
            arena.append(list(linha))
        s = input()        
        for c in s:
            if c == 'D':
                pi[2] = turn_right[pi[2]]
            elif c == "E":
                pi[2] = turn_left[pi[2]]
            else:
                line = pi[0]            
                column = pi[1]
                if pi[2] == "N":
                    line -= 1
                    if check_movement(line, column):
                        pi[0] -= 1                    
                elif pi[2] == "S":
                    line += 1
                    if check_movement(line, column):
                        pi[0] += 1            
                elif pi[2] == "L":
                    column += 1
                    if check_movement(line, column):
                        pi[1] += 1
                else:
                    column -= 1                
                    if check_movement(line, column):
                        pi[1] -= 1
        print(f)    